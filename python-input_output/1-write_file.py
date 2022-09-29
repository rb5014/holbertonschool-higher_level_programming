#!/usr/bin/python3
"""module containing a function write_file
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the
     number of characters written:
    must use the 'with' statement
    noo need to manage file permission
    should create file if doesn't exist
    should overwrite content of the file  if it already exists
    Args:
        filename (str, optional): file to read. Defaults to "".
    """
    with open(filename, 'w',  encoding="utf-8") as f:
        return f.write(text)
