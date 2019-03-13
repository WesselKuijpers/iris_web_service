from sqlalchemy import Column, Integer, Text
from sqlalchemy.exc import InvalidRequestError

from db.db import Base, Session


class Model(Base):
    __tablename__ = 'models'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    location = Column(Text, nullable=False)

    #TODO: move these to some abstract mapper class to keep the codebase DRY
    def save(self):
        session = Session()
        session.add(self)
        try:
            session.commit()
            return True
        except InvalidRequestError:
            return False

    def find_by_id(self, identifier):
        item = Session().query(Model).filter(Model.id == identifier).one()
        return {"id" : item.id, "name" : item.name, "location" : item.location}

    def all(self):
        items = Session().query(Model).all()
        result = []
        for item in items:
            model = {"id" : item.id, "name" : item.name, "location" : item.location}
            result.append(model)
        
        return result