# Hyperboria

## Introduction

Hyperboria repository is a pack of tools for dealing with SciMag and SciTech collections.

It consists of configurable [`search engine`](nexus/cognitron), [`pipeline`](nexus/pipe) for [`ingesting`](nexus/ingest) data
from upstream sources. So-called [`actions`](nexus/actions) aimed to converting data from external APIs
into [`internal Protobuf format`](nexus/models) and to landing converted data into databases and/or search engines.

## Prerequisite

### Ubuntu 20.04

#### Docker
[Installation Guide](https://docs.docker.com/engine/install/ubuntu/)

#### System Compilers
```shell script
sudo apt-get install -y --no-install-recommends g++ python3.9 protobuf-compiler libprotobuf-dev
```

#### Bazel Build System
[Installation Guide](https://docs.bazel.build/versions/master/install-ubuntu.html) or _one-liner_:
```shell script
sudo apt install curl gnupg
curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > bazel.gpg
sudo mv bazel.gpg /etc/apt/trusted.gpg.d/
echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
sudo apt update && sudo apt install bazel
```

#### IPFS
[Installation Guide](https://docs.ipfs.io/install/)

### MacOS

#### Docker
[Installation Guide](https://docs.docker.com/docker-for-mac/install/)

#### System Compilers
```shell script
brew install llvm protobuf python3.9
```

#### Bazel Build System
[Installation Guide](https://docs.bazel.build/versions/master/install-os-x.html) or _one-liner_:
```shell script
brew install bazel
```

#### IPFS
[Installation Guide](https://docs.ipfs.io/install/)

## Content

- [`images`](images) - base docker images for [`nexus`](nexus)
- [`library`](library) - shared libraries
- [`nexus`](nexus) - processing and searching in scientific text collections
- [`rules`](rules) - build rules