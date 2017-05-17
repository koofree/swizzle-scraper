import os
import json


class Writer:
    def __init__(self, config, name="UNKNOWN"):
        self.root_path = config['file']['path']
        self.name = name

        if not os.path.exists(self.root_path):
            os.makedirs(self.root_path)

        self.path = os.path.join(self.root_path, name)
        pass

    def write(self, review):
        with open(self.path, 'a', encoding='utf-8') as file:
            file.write(json.dumps(review, ensure_ascii=False))
            file.write("\n")
        pass
