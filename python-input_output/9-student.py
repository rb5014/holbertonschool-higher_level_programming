#!/usr/bin/python3
"""module containing the Class Student
"""


class Student:
    """class student containing the firstname, lastname and age of a student
    and the method to_json that retrieves the dictionnary representation of 
    a 'Student' instance
    """
    def __init__(self, first_name, last_name, age):
        """Instanciation of the public variables
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
