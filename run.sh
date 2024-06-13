#!/bin/bash

# Install dependencies
python -m pip install -r requirements.txt

# Create database
python -c "from crawler.database import db_session; db_session.create_all()"

# Run crawler
python -c "from crawler.crawler import Crawler; crawler = Crawler('https://example.com'); crawler.crawl()"

# Run tests
python -m unittest discover -v tests
