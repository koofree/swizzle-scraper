class Writer:
    def __init__(self, config, name="UNKNOWN"):
        self.name = name
        pass

    def write(self, review):
        self._print_console(self.name + ": " + str(review))
        pass

    @staticmethod
    def _print_console(review):
        print(review)
