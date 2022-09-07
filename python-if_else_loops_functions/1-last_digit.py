#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = int(repr(number)[-1])
if number < 0:
    lastdigit = -lastdigit
print(f"Last digit of {number} is {lastdigit}", end=' ')
if lastdigit > 5:
    print("and is greater than 5")
elif lastdigit == 0:
    print("and is zero")
else:
    print("and is less than 6 and not 0")
int(repr(number)[-1])
