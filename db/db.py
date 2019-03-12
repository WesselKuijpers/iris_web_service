from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import pymysql

# configure driver
pymysql.install_as_MySQLdb()

# make connection
# TODO: fetch connection string from configfile, or build it dynamically
engine = create_engine('mysql://root:aeH8ieja@localhost:3306/iris_webservice', echo=True)

# Instantiate base class
# the base class is extended by all map classes
# Is called in the deploy script with the engine to forward all the schemas to the database
Base = declarative_base()