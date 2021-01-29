# Nexus Cognitron

## Guide

#### 1. Download data dumps

```shell script
export COLLECTION=bafykbzacebzohi352bddfunaub5rgqv5b324nejk5v6fltjh45be5ykw5jsjg
export COLLECTION_PATH=$(realpath $COLLECTION)
ipfs get $COLLECTION
```

#### 2. Launch Nexus Cognitron

```shell script
cd nexus/cognitron
docker-compose up
```

#### 3. (Optional) Deploy data dumps into your database

There is a function `work` in [`traversing script`](installer/scripts/iterate.py)
that you can reimplement to iterate over the whole dataset and insert it into your
own database or do whatever you want in parallel mode.

By default this script is just printing documents.

```shell script
bazel run -c opt installer -- iterate \
  --store-filepath scitech.store.tar \
  --schema-filepath schema/scitech.yaml
```
