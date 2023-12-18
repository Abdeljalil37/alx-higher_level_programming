#!/usr/bin/python3
"""lists all State objects that contain the letter a from the database"""

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    contains_a = session.query(State).filter(State.name.contains('a')).all()
    for state in contains_a:
        print("{}: {}".format(state.id, state.name))
    session.close()
