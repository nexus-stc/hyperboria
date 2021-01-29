import yaml
from tantipy import TantivyCoder

with open('nexus/cognitron/schema/scitech.yaml') as file:
    scitech_coder = TantivyCoder(yaml.safe_load(file.read()))
