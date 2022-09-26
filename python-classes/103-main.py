#!/usr/bin/python3
from dis import dis
Circle = __import__('103-magic_class').MagicClass

c = Circle()
print()
print(c.area())
print()
print(c.circumference())
print()
print(dis(Circle))
