# Roadmap v.0.1

This paper is composed of lifetime goals for Nexus STC (Standard Template Construct).

Although many of goals looks complex and faraway I strongly believe that we will be able to survive and prosper only by making impossible things.

#### Legend
- (*) Big theoretical task
- (E) Non-essential but still worth to try

## Accessibility of Science

### Software Accessibility

#### Infrastructure

- Hermetic and reproducible build of `hyperboria` project
- Publishing slim images of all required parts to DockerHub (via public services)
- Mirroring repository to IPFS
- Modern one-click app in .deb, .dmg, .exe and Docker format with support of updates

#### Public Mirrors

- (E) Create Yggdrasil configuration
- (E) Promote Yggdrasil itself
- Create Onion configuration
- Discuss the possibility of switching original LibGen backend to Nexus

### Data Accessibility

#### Infrastructure

- Putting scimag collection onto IPFS
- Announce data dumps for both scitech and scimag collections
- Pinning feature in the app that will allow users to pin subset of the collection in an easy way
- (*) Consider various **reliable** ways to announce new releases of **initial** data dumps
- Maintain and curate the list of already publicly available journals in Pylon

### Decentilized Publishing

#### Search Server Prerequesties

- Reconsider search schema taking into account new conditions and points of current section
- `Writing API` in Summa/Tantivy that supports immutability of already existing data
- (*) Consider various ways to produce reproducible segments/chunks of data in the case when same records come in different order
- `Replication API` in Summa allowing to effectively stream records from one replica to another
- `Signing API` in Summa for signing every search record and allowing to check signature during replication
- (*) Consider various ways of records broadcasting without coordination

#### Establishing replication network

- Containerize `nexus-pipe` for ingesting feed from CrossRef
- Carry tests with several ingesting leader nodes and multiple replicants

## Observability of Science

### Massive OCR

- (E) Fork/take Grobid project under curation
- Pair Summa server with possibility to OCR
- Extend schema with full article content
- Find CPU capacities to OCR all legacy papers

### References

- Maintain graph statistics (at least PageRank) in Summa/Meta API
- Clickable reference links in Cognitron Web (as in the bot)

### Entity Extraction

- (*) Consider tools like SciBERT and other upcoming techs for automated entity recognition 
- Separate indexing for entity and navigation on them

### Usage Statistics

- (*) Consider various **reliable** ways of exchaning reading/downloading statistics of papers

### Broadcasting

- (*) Make new papers visible to relevant users

## Automated Science (to be done)

## Technology Alliance (to be done)
