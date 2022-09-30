#!/usr/bin/python3
"""module containing the Class Student (based on 10-student.py)
"""


class Student:
    """class student containing the firstname, lastname and age of a student
    and:
        the method to_json that retrieves the dictionnary representation of
    a 'Student' instance
        the method reload_from_json that replaces all attributes of the
    'Student' instance:
                        json always a dictionnary
                        dict key will be public attr name
                        dict value will be val of public attr
    """
    def __init__(self, first_name, last_name, age):
        """Instanciation of the public variables
        """
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        return {k: v for k, v in vars(self).items() if
                (attrs and k in attrs) or type(attrs) is not list}

    def reload_from_json(self, json):
        for k in vars(self).keys():
            for kj in json.keys():
                if k == kj:
                    vars(self)[k] = json[kj]
