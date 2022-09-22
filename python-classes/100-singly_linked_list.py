#!/usr/bin/python3
"""class Node that defines a node of a singly linked list by:

Private instance attribute: data:
property def data(self): to retrieve it
property setter def data(self, value): to set it:
data must be an integer, otherwise raise a TypeError exception with the
message data must be an integer
Private instance attribute: next_node:
property def next_node(self): to retrieve it
property setter def next_node(self, value): to set it:
next_node can be None or must be a Node, otherwise raise a TypeError exception
with the message next_node must be a Node object
Instantiation with data and next_node:
def __init__(self, data, next_node=None):
And, write a class SinglyLinkedList that defines a singly linked list by:

Private instance attribute: head (no setter or getter)
Simple instantiation: def __init__(self):
Should be printable:
print the entire list in stdout
one node number by line
Public instance method: def sorted_insert(self, value): that inserts a new
Node into the correct sorted position in the list (increasing order)
You are not allowed to import any module
"""


class Node:
    """_summary_ Class of the node
    """
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def next_node(self, value):
        if type(value) != Node and value:
            raise TypeError("next_node must be a Node object")
        else:
            self.__data = value


class SinglyLinkedList:
    """_summary_ class of the singly linked list
    """
    def __init__(self):
        self.__head = []

    def __str__(self):
        result = ""
        flag = False
        for i in self.__head:
            if flag is True:
                result += "\n"
            result += f"{i}"
            flag = True
        return result

    def sorted_insert(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__head.append(value)
        self.__head.sort()
