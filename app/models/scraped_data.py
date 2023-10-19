from sqlalchemy import Column, Integer, String
# from .base_model import Base

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ScrapedData(Base):
    __tablename__ = 'scraped_data'

    id = Column(Integer, primary_key=True)
    url = Column(String(), nullable=False)
    body = Column(String(), nullable=False)
    title = Column(String(512), nullable=False)