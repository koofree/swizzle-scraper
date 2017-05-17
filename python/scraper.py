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

    package_name = config_json['scrapers'][scraper_name]['package']
    connector_name = config_json['scrapers'][scraper_name]['connector']
    writer_name = config_json['scrapers'][scraper_name]['writer']
    limit_count = config_json['scrapers'][scraper_name]['limit']

    conn = importlib.import_module('connectors.' + connector_name).Connector(config_json['connectors'])
    writer = importlib.import_module('writers.' + writer_name).Writer(config_json['writers'], name=target_id)
    scraper = importlib.import_module('scrapers.' + package_name).Scraper(conn.api())
    for item in scraper.scrape(target_id, limit=limit_count):
        writer.write(item)
