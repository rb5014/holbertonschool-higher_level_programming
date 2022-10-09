#!/usr/bin/python3
"""module containing the function append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing
    a specific string

    Args:
        filename (str, optional): _description_. Defaults to "".
        search_string (str, optional): _description_. Defaults to "".
        new_string (str, optional): _description_. Defaults to "".
    """

    with open(filename, 'r+', encoding="utf-8") as f:
        lineList = f.readlines()
        f.seek(0)
        for i, line in enumerate(lineList):
            if search_string in line and line != new_string:
                lineList.insert(i + 1, new_string)
            f.write(line)
