import yaml
from tantipy import TantivyCoder

with open('nexus/cognitron/schema/scimag.yaml') as file:
    scimag_coder = TantivyCoder(yaml.safe_load(file.read()))
