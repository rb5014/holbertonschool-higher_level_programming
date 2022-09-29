#!/usr/bin/python3
"""module containing a function append_write
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and returns the
    number of characters added.
    create file if it doesn't exist
    must use the 'with' statement
    noo need to manage file permission or file doesn't exist exceptions
    Args:
        filename (str, optional): file to append text in. Defaults to "".
        text: text to append
    """
    with open(filename, 'a',  encoding="utf-8") as f:
        return f.write(text)
