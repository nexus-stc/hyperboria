# Hyperboria

## Introduction

Hyperboria repository is a pack of tools for dealing with SciMag and SciTech collections.

It consists of configurable [`search engine`](nexus/cognitron), [`pipeline`](nexus/pipe) for [`ingesting`](nexus/ingest) data
from upstream sources. So-called [`actions`](nexus/actions) aimed to converting data from external APIs
into [`internal Protobuf format`](nexus/models) and to landing converted data into databases and/or search engines.

## Prerequisite

Install system packages for various OSes:
```shell script
sudo ./repository/install-packages.sh
```

### Ubuntu 20.04

#### Docker
[Installation Guide](https://docs.docker.com/engine/install/ubuntu/)

#### IPFS
[Installation Guide](https://docs.ipfs.io/install/)

### MacOS

#### Docker
[Installation Guide](https://docs.docker.com/docker-for-mac/install/)

#### IPFS
[Installation Guide](https://docs.ipfs.io/install/)

## Content

- [`images`](images) - base docker images for [`nexus`](nexus)
- [`library`](library) - shared libraries
- [`nexus`](nexus) - processing and searching in scientific text collections
- [`rules`](rules) - build rules