import unittest
from crawler.database import db_session

class TestDatabase(unittest.TestCase):
    def test_create_all(self):
        db_session.create_all()
        # assert something