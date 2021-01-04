import yaml
from tantipy import TantivyCoder

with open('nexus/summa/schema/scimag.yaml') as file:
    scimag_coder = TantivyCoder(yaml.safe_load(file.read()))
