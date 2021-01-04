# Summa Setup Scripts

## Guide

#### 1. Find data dumps

Current version: `20210103.1`

| File                | IPFS                                             |
| --------------------|:------------------------------------------------:|
| `scitech.index.tar` | `QmVaWFRNTHC3ser4ViHybcD7nuhv2CUAorhXs4JbYYHYm7` |
| `scitech.store.tar` | `QmP3p577gRokXXtusRYXXV7MtF3pVmGSdNEUE5TwFzRtAm` |
| `scimag.index.tar`  | `<upcoming>`                                     |
| `scimag.store.tar`  | `<upcoming>`                                     |

If files are not available ask guys from beyond the blackwall.

#### 2. Deploy data dumps to Summa

```shell script
bazel run -c opt installer -- import-to-summa \
  --store-filepath scimag.store.tar \
  --index-filepath scimag.index.tar \
  --schema-filepath schema/scimag.yaml \
  --database-path /tmp/summa
bazel run -c opt installer -- import-to-summa \
  --store-filepath scitech.store.tar \
  --index-filepath scitech.index.tar \
  --schema-filepath schema/scitech.yaml \
  --database-path /tmp/summa
```

#### 3. Launch Summa

```shell script
docker run -e ENV_TYPE=production \
  -v /tmp/summa:/summa -v $(realpath configs/config.yaml):/summa/config.yaml \
  -p 50000:80 izihawa/summa:latest -c /summa/config.yaml
```

#### 4. Use it

```shell script
curl "localhost:50000/v1/scitech/search/?query=covid&page_size=2" | python3 -m json.tool
```
```json
{
    "has_next": true,
    "scored_documents": [
        {
            "schema": "scitech",
            "document": {
                "authors": [
                    "National committee for Management of COVID-19 Cases (Dubai Health Authority)"
                ],
                "cu_suf": "g",
                "description": "Objectives\r\nThe objectives of this document are:\r\n\u2022 To provide guidance on clinical management of the COVID-19 infection\r\n\u2022 To provide a protocol on the practical steps to deal with COVID-19 cases\r\n\u2022 To detail the measures necessary to protect hospital staff, patients and visitors\r\n\u2022 This guideline is not intended to override the clinical decisions that will be made by clinicians providing individualized patient care.\r\n\u2022 This guideline will be updated as more information becomes available.\r\nIntroduction to Coronaviruses (CoV)\r\n\u2022 Corona virus is a large family of viruses that cause illness in humans and animals\r\n\u2022 In people, CoV can cause illness ranging in severity from the common cold to SARS.\r\n\u2022 SARS COV2 is one of seven types of known human coronaviruses. SARS COV2 like the MERS and SARS coronaviruses, likely evolved from a virus previously found in animals\r\n\u2022 The estimated incubation period is unknown and currently considered to be up to 14 days\r\nCase Definition:\r\nSuspected COVID-19 case is defined as:\r\n1. Please refer to the local health authority websites for updated information on local case definition.\r\nMOHAP, DoH, SEHA and DHA\r\nConfirmed COVID-19 is defined as:\r\nA person with confirmed positive COVID-19 test by a reference laboratory.",
                "extension": "pdf",
                "filesize": 2240001,
                "id": 100126757,
                "ipfs_multihashes": [
                    "bafykbzacebasnsyh4sypqcojwmsd7ujw3ymogwhnx5vhywk7syptxovkyyzvk",
                    "QmSd3tYXxJnWzm8vxpW1M6uxLhvBSpSLQd7cHjdsaoE38D"
                ],
                "issued_at": 1577836800,
                "language": "en",
                "libgen_id": 2492432,
                "md5": "faf8bcab6ce58a59b3ed09f1e1d9270e",
                "tags": [
                    "COVID-19 Treatment"
                ],
                "title": "National Guidelines for Clinical Management and Treatment of COVID-19 (March 19, 2020) Version 1.1"
            },
            "score": 36.404663
        },
        {
            "schema": "scitech",
            "document": {
                "authors": [
                    "Dr. Tinku Joseph, Dr. Mohammed Ashkan"
                ],
                "cu_suf": "g",
                "description": "Corona virus comprises of a large family of viruses that are common in human beings as\r\nwell animals (camels, cattle, cats, and bats). There are seven different strains of corona\r\nvirus. [15]\r\n229E (alpha coronavirus)\r\nNL63 (alpha coronavirus)\r\nOC43 (beta coronavirus)\r\nHKU1 (beta coronavirus)\r\nMERS-CoV (the beta coronavirus that causes Middle East Respiratory Syndrome, or\r\nMERS)\r\nSARS-CoV (the beta coronavirus that causes severe acute respiratory syndrome, or\r\nSARS)\r\nSARS-CoV-2 (the novel coronavirus that causes coronavirus disease 2019, or\r\nCOVID-19)\r\nSometimes corona virus from animals infect people and spread further via human to human\r\ntransmission such as with MERS-CoV, SARS-CoV, and now with this COVID 19 (Corona\r\ndisease 2019). The virus that causes COVID-19 is designated severe acute respiratory\r\nsyndrome corona virus 2 (SARS-CoV-2); previously, referred to as 2019-nCoV.\r\nTowards December 2019, this novel corona virus was identified as a cause of upper and\r\nlower respiratory tract infections in Wuhan, a city in the Hubei Province of China. It rapidly\r\nspread, resulting in an epidemic throughout China and then gradually spreading to other\r\nparts of the world in pandemic proportions. It has affected almost every continent in this\r\nworld, except Antarctica. In February 2020, the World Health Organization designated the\r\ndisease COVID-19, which stands for corona virus disease 2019 [1].",
                "extension": "pdf",
                "filesize": 1512761,
                "id": 100110426,
                "issued_at": 1577836800,
                "language": "en",
                "libgen_id": 2494250,
                "md5": "23015d4934b216fe797b18b561267fe4",
                "pages": 43,
                "tags": [
                    "COVID-19"
                ],
                "title": "International Pulmonologist\u2019s Consensus on COVID-19"
            },
            "score": 32.969494
        }
    ]
}
```

#### 5. (Optional) Deploy data dumps into your database

There is a function `work` in [`traversing script`](installer/scripts/iterate.py)
that you can reimplement to iterate over the whole dataset and insert it into your
own database or do whatever you want in parallel mode.

By default this script is just printing documents.

```shell script
bazel run -c opt installer -- iterate \
  --store-filepath scitech.store.tar \
  --schema-filepath schema/scitech.yaml
```
