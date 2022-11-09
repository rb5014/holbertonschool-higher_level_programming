#!/usr/bin/python3
""" adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
from sys import argv as a
from model_state import Base, State

from sqlalchemy import create_engine, Table, Column
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(a[1], a[2], a[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    updated_state = session.get(State, 2)
    updated_state.name = "New Mexico"

    session.close()
