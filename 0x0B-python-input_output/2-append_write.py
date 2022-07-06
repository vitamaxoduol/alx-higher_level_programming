#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends into a file"""

    with open(filename, "a", encoding="utf-8") as file:
        return (file.write(text))
