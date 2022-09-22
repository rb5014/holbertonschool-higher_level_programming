#!/usr/bin/python3
""" class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

>Private instance attribute: width:
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
if width is less than 0, raise a ValueError exception with the message width must be >= 0

>Private instance attribute: height:
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
if height is less than 0, raise a ValueError exception with the message height must be >= 0
>Instantiation with optional width and height: def __init__(self, width=0, height=0):
"""

class Rectangle:
	""" Rectangle - defines a rectangle
	"""
	def __init__(self, width=0, height=0):
		# Initilize the rectangle
		self.height = height
		self.width = width

  
	@property
	def width(self):
		return self.__width
	
	@width.setter
	def width(self, value):
		try:
			self.__width = int(value)
		except TypeError:
			raise TypeError("width must be an integer")
		if self.__width < 0:
			raise ValueError("width must be >= 0")
		self.__width = int(value)

	@property
	def height(self):
		return self.__height
	
	@height.setter
	def height(self, value):
		try:
			self.__height = int(value)
		except TypeError:
			raise TypeError("height must be an integer")
		if self.__height < 0:
			raise ValueError("height must be >= 0")
		self.__height = int(value)
    