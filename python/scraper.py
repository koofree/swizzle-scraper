"""This is execution module for running scrapers.
This module support multiple type of scrapers.
The config.json file has information about how to run scraper. 
"""
from __future__ import print_function

import os
import json
import sys
import importlib

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(ROOT_DIR, '../config.json'), 'r') as config_file:
    config_json = json.load(config_file)


def scrape(_scraper_name, _target_id):
    package_name = config_json['scrapers'][_scraper_name]['package']
    connector_name = config_json['scrapers'][_scraper_name]['connector']
    writer_name = config_json['scrapers'][_scraper_name]['writer']
    limit_count = config_json['scrapers'][_scraper_name]['limit']
    model_name = None
    if 'model' in config_json['scrapers'][_scraper_name]:
        model_name = config_json['scrapers'][_scraper_name]['model']

    conn = importlib.import_module('connectors.' + connector_name).Connector(config_json['connectors'])
    writer = importlib.import_module('writers.' + writer_name).Writer(config_json['writers'], name=_target_id)
    scraper = importlib.import_module('scrapers.' + package_name).Scraper(conn.api())
    model = None
    if model_name:
        model = importlib.import_module('models.' + model_name).Model

    for item in scraper.scrape(_target_id, limit=limit_count):
        if model:
            from_func = getattr(model, "from_" + connector_name)
            t = from_func(item)
            writer.write(t)
        else:
            writer.write(item)


if __name__ == '__main__':
    scraper_name = config_json['default']

    if len(sys.argv) < 3:
        if len(sys.argv) > 1 and scraper_name:
            target_id = sys.argv[1]
            pass
        else:
            print('This program must have 2 arguments at least.')
            sys.exit(1)
    else:
        scraper_name = sys.argv[1]
        target_id = sys.argv[2]

    scrape(scraper_name, target_id)
