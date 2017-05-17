# Swizzle Scraper

Packages for review scraping from multiple type of web sources.

### Requirement
- [python3.6](https://www.python.org/downloads)

### Setup
    Make new config.json file on the project root folder using config.template.json file.
    In config.json file, write the connect informations for each apis.
    Run program using scripts or python codes.

### How to run with python code
    python python/setup.py install # Install dependencies (It can be required root permission)
    python python/scraper.py {scaper package name} {target id}

### How to run using scripts
    scripts/setup.bat # Install dependencies (It can be required root permission) 
    scripts/scrape.bat {scaper package name} {target id} 

### Supported scraper packages
    youtube_video_comment : Scraping youtube comments on a video. Target id is video id.
    facebook_page_comment : Scraping facebook comments on a page. Target id is page id.
    facebook_group_comment : Scraping facebook comments on a group. Target id is group id.
     
### Do you want more then scrapers? Contact to one of these.

- My email address : [koo@getswizzle.com](mailto:koo@getswizzle.com) 
- My company : [Swizzle Global](http://getswizzle.com) 