from db.db import engine, Base

# base class imports
from map_classes import model, log

class Deployer:
    def forward_schema(self):
        # call the map_classes
        # TODO: dyamic for all map_classes in the the map_classes folder.
        model.Model()
        log.Log()

        # create the schema's
        Base.metadata.create_all(engine)