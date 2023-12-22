#!/usr/bin/python3

""" prints the State object with the name passed as argument from the database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for data in (session.query(State.name, City.id, City.name)
                 .filter(State.id == City.state_id)):
        print(data[0] + ": (" + str(data[1]) + ") " + data[2])
    session.close()
