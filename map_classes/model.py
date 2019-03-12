from sqlalchemy import Column, Integer, Text
from sqlalchemy.exc import InvalidRequestError

from db.db import Base, Session


class Model(Base):
    __tablename__ = 'models'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    location = Column(Text, nullable=False)

    #TODO: move this to some abstract mapper class to keep the codebase DRY
    def save(self):
        session = Session()
        session.add(self)
        try:
            session.commit()
            return True
        except InvalidRequestError:
            return False
