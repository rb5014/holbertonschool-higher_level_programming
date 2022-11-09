#!/usr/bin/python3
""" lists all State objects that contain the letter a from
the database hbtn_0e_6_usa"""
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

    result = session.query(State).filter(State.name.contains('a')).all()

    for r in result:
        print("{}: {}".format(r.id, r.name))
