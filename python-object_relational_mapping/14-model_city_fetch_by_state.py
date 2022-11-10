#!/usr/bin/python3
""" prints all City objects from the database hbtn_0e_14_usa:
"""
from sys import argv as a
from model_state import Base, State
from model_city import City

from sqlalchemy import create_engine, Table, Column
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(a[1], a[2], a[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.name, City.id, City.name).filter(
        City.state_id == State.id).all()

    for row in result:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
    session.commit()
    session.close()
