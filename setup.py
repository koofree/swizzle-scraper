# -*- coding: utf-8 -*-

from setuptools import setup
from pip.req import parse_requirements

install_requirements = parse_requirements('requirements.txt', session='hack')
requirements = [str(ir.req) for ir in install_requirements]

with open('README.md') as f:
    readme = f.read()

setup(
    name='swizzle_scraper',
    version='0.1.0',
    description='Packages for multiple web scraping',
    long_description=readme,
    author='Koo Lee',
    author_email='koo@getswizzle.com',
    include_package_data=True,
    packages=['connectors', 'scrapers'],
    package_dir={
        'connectors': 'python/connectors',
        'scrapers': 'python/scrapers'
    },
    package_data={
        'swizzle_labs': ['*.ini',
                         'export/template/*.html']
    },
    install_requires=requirements
)
