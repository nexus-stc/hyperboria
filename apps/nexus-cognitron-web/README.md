## Prerequisite

Follow the [development guide](../../papers-please/99-development.md) to install Docker and IPFS.

## Guide

#### 1. Download data dumps

```shell script
git clone https://github.com/nexus-stc/hyperboria
cd hyperboria/apps/nexus-cognitron-web
export COLLECTION=bafykbzacebzohi352bddfunaub5rgqv5b324nejk5v6fltjh45be5ykw5jsjg
ipfs get $COLLECTION -o data && ipfs pin add $COLLECTION
export DATA_PATH=$(realpath ./data)
```

#### 2. Launch

```shell script
docker-compose pull && docker-compose up
```
then go to [http://localhost:3000](http://localhost:3000)