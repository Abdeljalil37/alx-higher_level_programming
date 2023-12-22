#!/usr/bin/python3
"""script that prints the State object with
 the name passed as argument from the database"""

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    Isexists = session.query(State).filter(State.name == argv[4],)
    try:
        print(Isexists[0].id)
    except IndexError:
        print("Not found")
    session.close()
