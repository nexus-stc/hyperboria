# Nexus Pipe

`Pipe` processes Kafka queue of operations. This version has cut `configs`
subdirectory due to hard reliance of configs on the network infrastructure you are using.
You have to write your own configs taking example below into account.

## Sample `configs/base.yaml`

```yaml
---
log_path: '/var/log/nexus-pipe/{{ ENV_TYPE }}'
pipe:
  brokers: |
    kafka-0.example.net,
    kafka-1.example.net
  schema:
    - consumers:
        - class: nexus.pipe.consumers.CrossReferencesBulkConsumer
          topics:
            - name: cross_references
              workers: 4
      group_id: pipe
      processors:
        - class: nexus.pipe.processors.CrossReferencesProcessor
          kwargs:
            brokers: |
              kafka-0.example.net,
              kafka-1.example.net
            database:
              database: nexus
              host: postgres.example.net
              password: '{{ DATABASE_PASSWORD }}'
              username: '{{ DATABASE_USERNAME }}'
    - consumers:
        - class: nexus.pipe.consumers.DocumentOperationsJsonConsumer
          topics:
            - name: operations
              workers: 2
        - class: nexus.pipe.consumers.DocumentOperationsConsumer
          topics:
            - name: operations_binary_hp
              workers: 4
            - name: operations_binary
              workers: 14
      group_id: pipe
      processors:
        - class: nexus.pipe.processors.ActionProcessor
          kwargs:
            actions:
              - class: nexus.actions.FillDocumentOperationUpdateDocumentScimagPbFromExternalSourceAction
                kwargs:
                  crossref:
                    rps: 50
                    user_agent: 'ScienceLegion/1.0 (Linux x86_64; ) ScienceLegion/1.0.0'
              - class: nexus.actions.CleanDocumentOperationUpdateDocumentScimagPbAction
              - class: nexus.actions.SendDocumentOperationUpdateDocumentScimagPbToGoldenPostgresAction
                kwargs:
                  database:
                    database: nexus
                    host: postgres.example.net
                    password: '{{ DATABASE_PASSWORD }}'
                    username: '{{ DATABASE_USERNAME }}'
              - class: nexus.actions.SendDocumentOperationUpdateDocumentScimagPbReferencesToKafkaAction
                kwargs:
                  brokers: |
                    kafka-0.example.net,
                    kafka-1.example.net
                  topic: cross_references
              - class: nexus.actions.SendDocumentOperationUpdateDocumentPbToSummaAction
                kwargs:
                  summa:
                    base_url: http://summa.example.net
                    timeout: 15
                    ttl_dns_cache: 30
            filter:
              class: nexus.pipe.filters.DocumentOperationFilter
              kwargs:
                document: scimag
                operation: update_document
        - class: nexus.pipe.processors.ActionProcessor
          kwargs:
            actions:
              - class: nexus.actions.CleanDocumentOperationUpdateDocumentScitechPbAction
              - class: nexus.actions.SendDocumentOperationUpdateDocumentScitechPbToGoldenPostgresAction
                kwargs:
                  database:
                    database: nexus
                    host: postgres.example.net
                    password: '{{ DATABASE_PASSWORD }}'
                    username: '{{ DATABASE_USERNAME }}'
              - class: nexus.actions.SendDocumentOperationUpdateDocumentPbToSummaAction
                kwargs:
                  summa:
                    base_url: http://summa.example.net
                    timeout: 15
                    ttl_dns_cache: 30
            filter:
              class: nexus.pipe.filters.DocumentOperationFilter
              kwargs:
                document: scitech
                operation: update_document
```