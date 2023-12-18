#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the database"""

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

    insert_line = State(name='Louisiana')
    session.add(insert_line)
    session.commit()
    print(insert_line.id)
    session.close()
