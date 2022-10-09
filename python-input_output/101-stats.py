#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics
"""
from pyexpat.errors import codes
import sys


def print_stats(fSize, dict):
    """print stats after each 10 lines or ctrl-c

    Args:
        fSize (int): total size
        dict (dict)): dict containing codes and the nb of occurences
    """
    print(f"File size: {fSize}")
    for key in sorted(dict.keys()):
        print(f"{key}: {dict[key]}")


codesDict = {}
fileSize = 0
count = 0

try:
    for x in sys.stdin:
        count += 1
        try:
            fileSize += int(x.split(' ')[8])
        except (IndexError, ValueError):
            continue
        try:
            key = int(x.split(' ')[7])
        except (IndexError, ValueError):
            continue
        if key in codesDict:
            codesDict[key] += 1
        else:
            codesDict[key] = 1
        if count == 10:
            count = 0
            print_stats(fileSize, codesDict)
except KeyboardInterrupt:
    raise
finally:
    print_stats(fileSize, codesDict)
