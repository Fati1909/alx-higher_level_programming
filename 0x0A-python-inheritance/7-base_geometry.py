#!/usr/bin/python3
"""class BaseGeometry"""

class BaseGeometry:
    """Represent base geometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate a parameter as an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
