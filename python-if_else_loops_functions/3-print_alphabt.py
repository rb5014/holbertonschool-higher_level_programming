#!/usr/bin/python3

for i in range(97, 123):
    if chr(i) != 'q' or 'e':
        print("{:c}" .format(i), end='')
