import json
from Config import Config

''' Write created objects to json file'''

c = Config()


class Output(object):

    def __init__(self):
        self.output = c.output()

    def create_json(self, objectList):
        output_file = json.dumps(objectList)
        with open(self.output, "w") as file:
            file.write(output_file)
