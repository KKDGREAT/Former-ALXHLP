#!/usr/bin/python3
""" Module contains a function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """returns the attributes and method of an object"""
    return dir(obj)
