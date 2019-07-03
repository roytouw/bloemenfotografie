import json


class ConfigLoader:

    def __init__(self):
        self.configFile = "config.json"
        self.snapshot_location = None

    def load_configuration(self):
        with open(self.configFile) as config:
            data = json.load(config)

        self.snapshot_location = data['fust_detection']['snapshot_location']


if __name__ == "__main__":
    cf = ConfigLoader()
    cf.load_configuration()
    print(cf.test)
