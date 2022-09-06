# Nexus Ingest

`Ingest` goes to Internet and send retrived data to Kafka queue of operations.
This version has cut `configs` subdirectory due to hard reliance of configs on the network infrastructure you are using.
You have to write your own configs taking example below into account.

## Sample `configs/base.yaml`

```yaml
---
jobs:
  crossref-api:
    class: nexus.ingest.jobs.CrossrefApiJob
    kwargs:
      actions:
        - class: nexus.actions.postgres.ToScimagPbAction
        - class: nexus.actions.scimag_pb.ToDocumentOperationBytesAction
          kwargs:
            full_text_index: true
            should_fill_from_external_source: true
      base_url: https://api.crossref.org/
      max_retries: 60
      retry_delay: 10
      sinks:
        - class: nexus.ingest.sinks.KafkaSink
          kwargs:
            kafka:
              bootstrap_servers:
                - kafka-0.example.net
              topic_name: operations_binary
  libgen-api:
    class: nexus.ingest.jobs.LibgenApiJob
    kwargs:
      actions:
        - class: nexus.actions.libgen_api.ToScitechPbAction
        - class: nexus.actions.scitech_pb.ToDocumentOperationBytesAction
          kwargs:
            full_text_index: true
            should_fill_from_external_source: false
      base_url: libgen.example.net
      max_retries: 60
      retry_delay: 10
      sinks:
        - class: nexus.ingest.sinks.KafkaSink
          kwargs:
            bootstrap_servers:
              - kafka-0.example.net
            topic_name: operations_binary
log_path: '/var/log/nexus-ingest/{{ ENV_TYPE }}'
```