#!/usr/bin/python3
"""
function that returns True if the object is an instance of, or if the object is an instance of a class.
"""

def is_kind_of_class(obj, a_class):
    """Check if an object is an instance."""
    if isinstance(obj, a_class):
        return True
    return False
