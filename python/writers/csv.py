import csv
import os


class Writer:
    def __init__(self, config, name="UNKNOWN"):
        self.root_path = config['csv']['path']
        self.name = name
        self.count = 0

        if not os.path.exists(self.root_path):
            os.makedirs(self.root_path)

        self.path = os.path.join(self.root_path, name)

        self.writer = None
        pass

    def write(self, review):
        if not self.writer:
            self.writer = csv.DictWriter(open(self.path, 'w', encoding='utf-8'), review.keys())
            self.writer.writeheader()
        self.writer.writerow(review)
        self.count += 1
        if self.count % 10 == 0:
            print(("Row %s was written." % self.count))
        pass
