#!/usr/bin/python3
"""script that deletes all State objects with a name containing
the letter a from the database """

from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    contains_a = session.query(State).filter(State.name.contains('a')).all()
    for state in contains_a:
        session.delete(state)
    session.commit()
    session.close()
