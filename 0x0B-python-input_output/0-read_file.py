#!/usr/bin/python3
"""Reads given file"""


def read_file(filename=""):
    """File"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())
