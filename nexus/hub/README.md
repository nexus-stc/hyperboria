# Nexus Search: Hub API

`Hub` is a daemon responsible for retrieving files and sending them to users. This version has cut `configs`
subdirectory due to hard reliance of configs on the network infrastructure you are using.
You have to write your own configs taking example below into account.

The bot requires two other essential parts: 
- Postgres Database
- IPFS Daemon

or their substitutions

## Sample `configs/base.yaml`

```yaml
---

application:
  # Look at the special Postgres `sharience` table to retrieve user-sent files
  is_sharience_enabled: true
  maintenance_picture_url:
  # Used in logging
  service_name: nexus-hub
  # Store file hashes into operation log
  should_store_hashes: true
database:
  database: nexus
  host:
  password: '{{ DATABASE_PASSWORD }}'
  username: '{{ DATABASE_USERNAME }}'
grobid:
  url:
grpc:
  # Listen address
  address: 0.0.0.0
  # Listen port
  port: 9090
ipfs:
  address:
  port: 4001
log_path: '/var/log/nexus-hub/{{ ENV_TYPE }}'
meta_api:
  url:
pylon:
  # Proxy used in `pylon` retriever to download files
  proxy: socks5://127.0.0.1:9050
  # Proxy used in `pylon` retriever to get metadata
  resolve_proxy: socks5://127.0.0.1:9050
telegram:
  # Telegram App Hash from https://my.telegram.org/
  app_hash: '{{ APP_HASH }}'
  # Telegram App ID from https://my.telegram.org/
  app_id: 00000
  # External bot name shown in messages to users
  bot_external_name: libgen_scihub_bot
  # Internal bot name used in logging
  bot_name: nexus-bot
  bot_token: '{{ BOT_TOKEN }}'
  # Telethon database for keeping cache
  database:
    session_id: nexus-hub
  # Frequency of updating downloading progress
  progress_throttle_seconds: 5
  # Send files using stored telegram_file_id
  should_use_telegram_file_id: true
```