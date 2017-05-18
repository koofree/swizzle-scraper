import mechanicalsoup as mechanize


class Connector:
    def __init__(self, config):
        self.br = mechanize.Browser()
        self.br.addheaders = [('User-agent', config['browser']['user_agent'])]

        self.connector = {
            "request": self.br.request,
            "post": self.br.post,
            "get": self.br.get
        }

    def api(self):
        return self.connector
