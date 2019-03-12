from db.db import Base, engine
from sqlalchemy import Column, Integer, Text

class Model(Base):
    __tablename__ = 'models'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    location = Column(Text)