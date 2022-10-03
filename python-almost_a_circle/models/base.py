#!/usr/bin/python3
""" module containing the class Base
"""
import json


class Base:
    """
    -'base' class of all other classes in this project
    -The goal of it is to manage id attribute in all future classes
    and to avoid duplicating the same code (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        # Instanciation of the class with the assignment of id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
