# Nexus Cognitron

## Prerequisite

Follow the [root guide](../../README.md) to install Docker, IPFS and Bazel (optionally)

## Guide

#### 1. Download data dumps

```shell script
export COLLECTION=bafykbzacebzohi352bddfunaub5rgqv5b324nejk5v6fltjh45be5ykw5jsjg
export COLLECTION_PATH=$(realpath $COLLECTION)
ipfs get $COLLECTION
```

#### 2. Launch Nexus Cognitron

Create [`docker-compose.yml`](docker-compose.yml) file to set up Nexus Cognitron and then launch it:
```shell script
docker-compose up
```
then go to [http://localhost:3000](http://localhost:3000)

#### 3. (Optional) Deploy data dumps into your database

There is a function `work` in [`traversing script`](installer/scripts/iterate.py)
that you can reimplement to iterate over the whole dataset and insert it into your
own database or do whatever you want in parallel mode.

By default this script is just printing documents.

```shell script
bazel run -c opt installer -- iterate \
  --data-filepath $COLLECTION_PATH/index/scitech \
  --schema-filepath schema/scitech.yaml
```
