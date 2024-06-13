import unittest
from crawler.models import Website, Page

class TestModels(unittest.TestCase):
    def test_website(self):
        website = Website(url='https://example.com')
        # assert something