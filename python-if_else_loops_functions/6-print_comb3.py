#!/usr/bin/python3

for i in range(0, 10):
    for j in range(0, 10):
        if i != j and i < j:
            if j > 1:
                print(", ", end='')
            print("{:02}" .format(i*10+j), end='')
print()
