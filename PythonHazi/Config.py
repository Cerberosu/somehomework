from pathlib import Path
import yaml

''' Reading and processing YAML.
    separating fields and data_file parts'''


class Config(object):

    def __init__(self):
        self.document_yaml = Path("./cfg.yaml").read_text()
        self.field_list = yaml.safe_load(self.document_yaml)["fields"]
        self.output_location = yaml.safe_load(self.document_yaml)["data_file"]

    def fields(self):
        return self.field_list

    def output(self):
        return self.output_location
