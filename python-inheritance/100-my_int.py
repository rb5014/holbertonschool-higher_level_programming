#!/usr/bin/python3
"""_summary_ module that contains the class MyInt that inherits from int
    """


class MyInt(int):
    """ MyInt is a rebel. MyInt has == and != operators inverted

    Args:
        int (_type_): type int
    """

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
