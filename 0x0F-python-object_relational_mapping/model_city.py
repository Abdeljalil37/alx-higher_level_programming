#!/usr/bin/python3
"""
Contains the class definition of a City
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base


class State(Base):
    """
    Class that defines each city
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


# Specify your MySQL connection details
DB_USER = argv[1]
DB_PASSWORD = argv[2]
DB_HOST = 'localhost'
DB_PORT = 3306
DB_NAME = argv[3]

# Create the MySQL engine
engine = create_engine(f"""mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@
                       {DB_HOST}:{DB_PORT}/{DB_NAME}""", pool_pre_ping=True)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example: Inserting a new state into the 'states' table
new_state = State(name='New State')
session.add(new_state)
session.commit()

# Example: Querying all states from the 'states' table
all_states = session.query(State).all()
for state in all_states:
    print(state.id, state.name)

# Close the session
session.close()
