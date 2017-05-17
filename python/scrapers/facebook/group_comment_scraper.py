from ._scraper import AbstractScraper


class Scraper(AbstractScraper):
    def __init__(self, connector):
        super().__init__(connector, 'group')
        pass
