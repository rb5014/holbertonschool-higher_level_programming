#!/usr/bin/python3
"""
model_state -  Python file similar to model_state.py named model_city.py that
contains the class definition of a City

"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """Class City that inherits from Base
        links to the MySQL table states
    class attribute id that represents a column of an auto-generated, unique
    integer, can’t be null and is a primary key
    class attribute name that represents a column of a string with maximum 128
    characters and can’t be null
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
