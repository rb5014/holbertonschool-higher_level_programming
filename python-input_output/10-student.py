#!/usr/bin/python3
"""module containing the Class Student (based on 9-student.py)
"""


class Student:
    """class student containing the firstname, lastname and age of a student
    and the method to_json that retrieves the dictionnary representation of
    a 'Student' instance
    """
    def __init__(self, first_name, last_name, age):
        """Instanciation of the public variables
        """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        return {k: v for k, v in vars(self).items() if
                (attrs and k in attrs) or not attrs}
