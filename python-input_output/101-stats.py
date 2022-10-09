#!/usr/bin/python3
import sys


def print_stats(fSize, dict):
    print(f"File size: {fSize}")
    for key in sorted(dict.keys()):
        print(f"{key}: {dict[key]}")


codesDict = {}
fileSize = 0
count = 0

try:
    for x in sys.stdin:
        if count == 10:
            count = 0
            print_stats(fileSize, codesDict)
        fileSize += int(x.split(' ')[8])
        key = x.split(' ')[7]
        if key in codesDict:
            codesDict[key] += 1
        else:
            codesDict[key] = 1
        count += 1
except KeyboardInterrupt:
    print_stats(fileSize, codesDict)
    raise
