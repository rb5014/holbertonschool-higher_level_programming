#!/usr/bin/python3
"""_summary_ module that contains the class MyList and function print_sorted
    """


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """Public instance method: def print_sorted(self): that prints the
            list, but sorted (ascending sort)
            all the elements of the list will be of type int
            """
        return sorted(self)
