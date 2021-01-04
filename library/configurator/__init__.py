import os
import os.path
from types import ModuleType

import orjson as json
import yaml
from izihawa_utils.common import smart_merge_dicts
from jinja2 import Template
from library.configurator.exceptions import UnknownConfigFormatError


class ConfigObject(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError as e:
            raise AttributeError(e)


class AnyOf:
    def __init__(self, *args):
        self.args = args


class RichDict(dict):
    def has(self, *args):
        current = self
        for c in args:
            if c not in current:
                return False
            current = current[c]
        return True

    def copy_if_exists(self, source_keys, target_key):
        current = self
        for c in source_keys:
            if c not in current:
                return False
            current = current[c]
        self[target_key] = current
        return True


class Configurator(RichDict):
    def __init__(self, configs: list):
        """
        Create Configurator object

        :param configs: list of paths to config files, dicts or modules.
        End filepath with `?` to mark it as optional config.
        """
        super().__init__()

        self._by_basenames = {}
        self._omitted_files = []

        env_config = {}
        env_config_var = os.environ.get('CONFIGURATOR', '')
        if env_config_var:
            env_config = yaml.safe_load(env_config_var)

        for config in ([os.environ] + configs + [env_config]):
            file_found = self.update(config)
            if not file_found:
                self._omitted_files.append(config)

    def _config_filename(self, filename):
        return os.path.join(os.getcwd(), filename)

    def walk_and_render(self, c):
        if isinstance(c, str):
            return Template(c).render(**self)
        elif isinstance(c, list):
            return [self.walk_and_render(e) for e in c]
        elif isinstance(c, dict):
            for key in c:
                c[key] = self.walk_and_render(c[key])
        return c

    def update(self, new_config, basename=None, **kwargs):
        if isinstance(new_config, AnyOf):
            for config in new_config.args:
                try:
                    return self.update(config.rstrip('?'))
                except IOError:
                    pass
            raise IOError('None of %s was found' % ', '.join(new_config.args))
        elif isinstance(new_config, str):
            optional = new_config.endswith('?')
            filename = new_config.rstrip('?')
            basename = basename or os.path.basename(filename)

            config_filename = self._config_filename(filename)

            data = None

            if os.path.exists(config_filename) and os.access(config_filename, os.R_OK):
                with open(config_filename) as f:
                    data = f.read()

            if data is None:
                if optional:
                    return False
                else:
                    raise IOError(f'File {config_filename} not found')

            if filename.endswith('.json'):
                new_config = json.loads(data)
            elif filename.endswith('.yaml'):
                new_config = yaml.safe_load(data)
            else:
                raise UnknownConfigFormatError(filename)

            new_config = self.walk_and_render(new_config)

        elif isinstance(new_config, ModuleType):
            new_config = new_config.__dict__

        elif callable(new_config):
            new_config = new_config(self)

        if not new_config:
            new_config = {}

        for k in new_config:
            if callable(new_config[k]):
                new_config[k] = new_config[k](context=self)

        if 'log_path' in new_config:
            new_config['log_path'] = os.path.expanduser(new_config['log_path']).rstrip('/')

        smart_merge_dicts(self, new_config, list_policy='override', copy=False)
        if basename:
            self._by_basenames[basename] = new_config

        return True

    def get_config_by_basename(self, basename):
        return self._by_basenames[basename]

    def get_object_by_basename(self, basename):
        return ConfigObject(self._by_basenames[basename])

    def has_missed_configs(self):
        return bool(self._omitted_files)

    def has_file(self, basename):
        return basename in self._by_basenames
