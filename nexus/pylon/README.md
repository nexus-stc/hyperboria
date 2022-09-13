# Nexus Pylon

`Pylon` is a downloader for scientific publications.
- Look articles by DOI, MD5 or IPFS hashes
- Validates downloaded items
- Streams data by chunks
- GRPC-ready

## Build

```bash
bazel build -c opt nexus-pylon-wheel
```

## Install

### PIP
```bash
pip install nexus-pylon
```

## Nexus Pylon CLI

Download scientific publication:
```bash
pylon download --doi 10.1182/blood-2011-03-325258 --output article.pdf
```

Download file by its MD5:
```bash
pylon download --md5 f07707ee92fa675fd4ee53e3fee977d1 --output article.pdf
```

Download file by its multihash:
```bash
pylon download --ipfs-multihashes '["bafykbzacea3vduqii3u52xkzdqan5oc54vsvedmed25dfybrqxyafahjl3rzu"]' --output article.pdf
```

### Using with Selenium

Create directory for exchaning files between host and launched Selenium in Docker
```bash
mkdir downloads
```

Launch Selenium in Docker
```bash
docker run -e SE_START_XVFB=false -v $(pwd)/downloads:/downloads -p 4444:4444 selenium/standalone-chrome:latest
```

Launch Pylon
```bash
pylon download --doi 10.1101/2022.09.09.507349 --output article.pdf \
--wd-endpoint 'http://127.0.0.1:4444/wd/hub' \
--wd-directory /downloads --wd-host-directory $(pwd)/downloads --debug
```