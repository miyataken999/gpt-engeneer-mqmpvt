from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///crawler.db')
Base = declarative_base()

class Database:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def create_all(self):
        Base.metadata.create_all(engine)

db_session = Database()