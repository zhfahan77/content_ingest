from sqlalchemy import Column, Integer, String, DateTime, text
from sqlalchemy.dialects.postgresql import JSON

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ScrapedData(Base):
    __tablename__ = 'scraped_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    domain = Column(String(128), nullable=False, index=True)
    path = Column(String(256), nullable=False)
    body = Column(String(), nullable=False)
    title = Column(String(512), nullable=False)
    metadata_json = Column(JSON)
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

    def __init__(self, domain, path, body, title, metadata_json):
        self.domain = domain
        self.path = path
        self.body = body
        self.title = title
        self.metadata_json = metadata_json
