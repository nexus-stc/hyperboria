#### Deploy data dumps into your database

There is a function `work` in [`traversing script`](installer/scripts/iterate.py)
that you can reimplement to iterate over the whole dataset and insert it into your
own database or do whatever you want in parallel mode.

By default this script is just printing documents.

```shell script
bazel run -c opt installer -- iterate \
  --data-filepath $DATA_PATH/index/scitech \
  --schema-filepath schema/scitech.yaml
```
