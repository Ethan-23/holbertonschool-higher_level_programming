#!/usr/bin/python3
"""object is an instance of, or if the object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """return true or false"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
