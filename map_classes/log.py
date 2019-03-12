from db.db import Base, engine
from sqlalchemy import Column, Integer, Text, DateTime

class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    content = Column(Text)