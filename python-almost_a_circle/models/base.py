#!/usr/bin/python3
""" module containing the class Base
"""
import json
import csv
from os.path import exists


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
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        obj = cls(1, 2, 0)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        if not exists(f"{cls.__name__}.json"):
            return []
        with open(f"{cls.__name__}.json", "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        header, data = cls.to_csv_header_data(list_objs)
        with open(f"{cls.__name__}.csv", "w", encoding="utf-8") as file:
            csvwriter = csv.writer(file)  # create a csvwriter object
            csvwriter.writerow(header)  # write the header
            csvwriter.writerows(data)  # write the rest of the data

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        rows = []
        if not exists(f"{cls.__name__}.csv"):
            return rows
        with open(f"{cls.__name__}.csv", "r", encoding="utf-8") as file:
            csvreader = csv.reader(file)  # creste a csvreader object
            header = next(csvreader)  # store a list of header's elements
            for row in csvreader:  # store a list of lists of the values
                rows.append(row)
            # convert header and rows into a list of dictionary representations
            # based on the csvreader object
            list_dict = cls.from_csv_header_data_to_list_dict(header, rows)
        return [cls.create(**d) for d in list_dict]

    @staticmethod
    def to_csv_header_data(list_objs):
        """returns the header and data lists of list_objs"""
        if list_objs is not None and len(list_objs) > 0:
            list_objs = [obj.to_dictionary() for obj in list_objs]
            header = [name for name in list_objs[0]]
            data = [[row[value] for value in row] for row in list_objs]
            return header, data
        else:
            return [], []

    @staticmethod
    def from_csv_header_data_to_list_dict(header, data):
        """returns the list of dictionnary representations of instances
        from header and data"""

        return [{header[i]: int(values[i]) for i in range(len(values))}
                for values in data]
