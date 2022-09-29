#!/usr/bin/python3
"""module containing a function readfile
"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout:
    must usethe 'with' statement
    noo need to manage file permission or file doesn't exist exceptions
    Args:
        filename (str, optional): file to read. Defaults to "".
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
