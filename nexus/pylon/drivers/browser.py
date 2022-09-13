import asyncio
import json
import logging
import os.path
import shutil
import time
from pathlib import Path
from typing import (
    Dict,
    List,
    Optional,
    Tuple,
)

import aiofiles
from izihawa_utils.random import random_string
from nexus.pylon.consts import DEFAULT_USER_AGENT
from nexus.pylon.drivers.base import BaseDriver
from nexus.pylon.exceptions import NotFoundError
from nexus.pylon.prepared_request import PreparedRequest
from nexus.pylon.proto.file_pb2 import Chunk as ChunkPb
from nexus.pylon.proto.file_pb2 import FileResponse as FileResponsePb
from nexus.pylon.proxy_manager import ProxyManager
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BrowserDriver(BaseDriver):
    def __init__(
        self,
        config,
        validator=None,
        proxy_list: Optional[List] = None,
        proxy_manager: Optional[ProxyManager] = None,
        actions: Optional[List] = None,
    ):
        super().__init__(config=config, validator=validator, proxy_list=proxy_list, proxy_manager=proxy_manager)
        self.actions = actions
        self.downloads_directory = Path(config['webdriver_hub']['downloads_directory'])
        self.host_downloads_directory = Path(config['webdriver_hub']['host_downloads_directory'])
        self.window_size = tuple(config['webdriver_hub'].get('window_size', [1279, 833]))
        self.erase_webdriver_property = config['webdriver_hub'].get('erase_webdriver_property', True)
        self.webdriver_hub_endpoint = config['webdriver_hub']['endpoint']
        self.file_poll_timeout = 2.0

    async def get_chrome_sessions(self):
        proxies = list(
            self.proxy_manager.get_proxies(self.proxy_list)
            if self.proxy_manager and self.proxy_list
            else [None]
        )
        for proxy in proxies:
            subdirectory = random_string(16)
            downloads_directory = self.downloads_directory / subdirectory
            host_downloads_directory = self.host_downloads_directory / subdirectory
            os.mkdir(host_downloads_directory)
            os.chmod(host_downloads_directory, 0o777)
            chrome = await asyncio.get_running_loop().run_in_executor(None, lambda: self.setup_chrome(proxy, downloads_directory))
            yield chrome, host_downloads_directory


    def setup_chrome(self, proxy, downloads_folder):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
            'download.default_directory': str(downloads_folder),
            'download.prompt_for_download': False,
            'safebrowsing.enabled': True,
            'plugins.always_open_pdf_externally': True,
            'profile.default_content_setting_values.automatic_downloads': True,
        })

        options.add_argument('user-agent=' + DEFAULT_USER_AGENT)

        if proxy:
            options.add_argument('--proxy-server=%s' % proxy.get_address())

        options.add_argument('--headless')
        options.add_argument('--enable-javascript')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--disable-popup-blocking")
        chrome = webdriver.Remote(
            self.webdriver_hub_endpoint,
            DesiredCapabilities.CHROME,
            options=options,
        )
        chrome.set_window_size(self.window_size[0], self.window_size[1])

        if self.erase_webdriver_property:
            resource = "/session/%s/chromium/send_command_and_get_result" % chrome.session_id
            url = chrome.command_executor._url + resource
            body = json.dumps({'cmd': "Page.addScriptToEvaluateOnNewDocument", 'params': {
                "source": """
                Object.defineProperty(navigator, 'webdriver', {
                  get: () => undefined
                })
              """
            }})
            chrome.command_executor._request('POST', url, body)

        logging.getLogger('nexus_pylon').debug({
            'action': 'start_chrome',
            'mode': 'pylon',
            'proxy': str(proxy) if proxy is not None else None,
            'downloads_folder': str(downloads_folder),
        })
        return chrome

    async def wait_for_file(self, path, timeout):
        start_time = time.time()
        while time.time() - timeout < start_time:
            file = self.get_first_file(path)
            if file:
                return file
            await asyncio.sleep(0.1)

    def get_first_file(self, path):
        files = os.listdir(path)
        if files:
            return str(Path(path) / files[0])

    async def produce_downloaded_file(self, downloads_folder, timeout=10.0, download_timeout=1200.0):
        filename = await self.wait_for_file(downloads_folder, timeout)
        if not filename:
            raise NotFoundError()

        current_offset = 0
        try:
            file = await aiofiles.open(filename, 'rb')
        except FileNotFoundError:
            file = await aiofiles.open(self.get_first_file(downloads_folder), 'rb')

        try:
            start_time = time.time()
            while time.time() - download_timeout < start_time:
                current_file = self.get_first_file(downloads_folder)

                await file.seek(0, os.SEEK_END)
                downloaded_offset = await file.tell()

                if (
                    not current_file.endswith('.crdownload')
                    and downloaded_offset == current_offset
                    and current_offset > 0
                ):
                    return
                await file.seek(current_offset)
                yield await file.read(downloaded_offset - current_offset)
                current_offset = downloaded_offset

                await asyncio.sleep(self.file_poll_timeout)
            raise NotFoundError()
        finally:
            await file.close()

    def get(self, chrome, url, params):
        logging.getLogger('nexus_pylon').debug({
            'action': 'download',
            'mode': 'pylon',
            'url': url,
        })
        try:
            chrome.get(url)
            if not self.actions:
                return True
            last_element = None
            previous_window = None
            current_window = chrome.window_handles[0]
            for action in self.actions:
                match action['type']:
                    case 'click':
                        if not last_element:
                            raise RuntimeError('Nothing to click')
                        chrome.execute_script("arguments[0].click();", last_element)
                    case 'close_window':
                        current_window = previous_window
                        previous_window = None
                        chrome.close()
                        chrome.switch_to.window(current_window)
                    case 'native_click':
                        if not last_element:
                            raise RuntimeError('Nothing to click')
                        last_element.click()
                    case 'switch_to_new_window':
                        previous_window = current_window
                        current_window = chrome.window_handles[-1]
                        chrome.switch_to.window(current_window)
                    case 'type':
                        if not last_element:
                            raise RuntimeError('Nothing to type')
                        last_element.clear()
                        last_element.send_keys(action['text'].format(**params))
                    case 'wait':
                        time.sleep(action['timeout'])
                    case 'wait_css_selector':
                        last_element = WebDriverWait(chrome, action.get('timeout', 15.0)).until(
                            EC.presence_of_element_located((
                                By.CSS_SELECTOR,
                                action['selector'],
                            ))
                        )
                    case 'wait_link_text':
                        last_element = WebDriverWait(chrome, action.get('timeout', 15.0)).until(
                            EC.presence_of_element_located((
                                By.LINK_TEXT,
                                action['selector'],
                            ))
                        )
                    case 'wait_xpath':
                        last_element = WebDriverWait(chrome, action.get('timeout', 15.0)).until(
                            EC.presence_of_element_located((
                                By.XPATH,
                                action['selector'],
                            ))
                        )
                    case _:
                        raise NotImplementedError('Not implemented action type')
        except WebDriverException as e:
            logging.getLogger('nexus_pylon').debug({
                'action': 'error',
                'mode': 'pylon',
                'error': str(e),
            })
            return False
        return True

    async def execute_prepared_file_request(self, prepared_file_request: PreparedRequest, params: Dict):
        async for chrome, downloads_folder in self.get_chrome_sessions():
            try:
                result = await asyncio.get_running_loop().run_in_executor(
                    None,
                    lambda: self.get(chrome, prepared_file_request.url, params),
                )

                if not result:
                    continue

                file_validator = self.validator(params)
                yield FileResponsePb(status=FileResponsePb.Status.BEGIN_TRANSMISSION, source=chrome.current_url)
                async for content in self.produce_downloaded_file(
                    downloads_folder,
                    timeout=prepared_file_request.timeout,
                    download_timeout=1200.0,
                ):
                    file_validator.update(content)
                    yield FileResponsePb(
                        chunk=ChunkPb(content=content),
                        source=chrome.current_url,
                    )
                file_validator.validate()
                return
            except NotFoundError:
                logging.getLogger('nexus_pylon').debug({
                    'action': 'no_response',
                    'mode': 'pylon',
                })
            finally:
                logging.getLogger('nexus_pylon').debug({
                    'action': 'quit_chrome',
                    'mode': 'pylon',
                })
                chrome.quit()
                shutil.rmtree(downloads_folder)
        raise NotFoundError(params=params, url=prepared_file_request.url, driver=str(self))
