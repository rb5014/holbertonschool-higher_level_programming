#!/usr/bin/python3
""" Module containing a function text_indentation
"""


def text_indentation(text=""):
    """ text_indentation - prints a text with 2 new lines after each of
        these characters: ., ? and :

        Parameters:
            @text: text must be a string, otherwise raise a TypeError exception
            with the message text must be a string

        There should be no space at the beginning or at the end of each
        printed line
    """
    afterDelim = False

    if not text or isinstance(text, str) is False:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] in ".?:":
            print(text[i]+"\n")
            afterDelim = True
        else:
            if afterDelim is False or text[i] != " ":
                print(text[i], end='')
                afterDelim = False
