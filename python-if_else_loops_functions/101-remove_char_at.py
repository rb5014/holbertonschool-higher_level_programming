#!/usr/bin/python3
def remove_char_at(str, n):
    if n == 0:
        cpystr = str[1:]
    elif n > 0:
        cpystr = str[:n] + str[n + 1:]
    else:
        cpystr = str
    return cpystr
