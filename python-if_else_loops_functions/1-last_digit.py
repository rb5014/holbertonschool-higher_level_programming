#!/usr/bin/python3
import random
number = int(random.randint(-10000, 10000))
lastdigit = number % 10 if number >= 0 else number % -10
print(f"Last digit of {number} is {lastdigit}", end=' ')
if lastdigit > 5:
    print("and is greater than 5")
elif lastdigit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
