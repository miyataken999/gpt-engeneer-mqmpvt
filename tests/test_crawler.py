import unittest
from crawler.crawler import Crawler

class TestCrawler(unittest.TestCase):
    def test_crawl(self):
        crawler = Crawler('https://example.com')
        crawler.crawl()
        # assert something