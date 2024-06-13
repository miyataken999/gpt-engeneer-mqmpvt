from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Website(Base):
    __tablename__ = 'websites'
    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)

class Page(Base):
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    website_id = Column(Integer, ForeignKey('websites.id'))
    website = relationship('Website', backref='pages')