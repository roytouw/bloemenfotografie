import json


class ConfigLoader:

    def __init__(self):
        self.configFile = "config.json"
        self.test = None

    def load_configuration(self):
        with open(self.configFile) as config:
            data = json.load(config)

        self.test = data['test']


if __name__ == "__main__":
    cf = ConfigLoader()
    cf.load_configuration()
    print(cf.test)
