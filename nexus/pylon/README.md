# Nexus Pylon

`Pylon` is a downloader for scientific publications.
- Look articles by DOI, MD5 or IPFS hashes
- Validates downloaded items
- Streams data by chunks
- GRPC-ready

## Nexus Pylon CLI

Casual download
```bash 
bazel run -c opt cli -- doi 10.1056/NEJMoa2033700 --output article.pdf
```

Download with proxies
```bash 
bazel run -c opt cli -- md5 278C3A72B7B04717361501B8642857DF \
  --output file.pdf \
  --proxies socks5://127.0.0.1:9050
```
