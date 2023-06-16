#!/usr/bin/python3
"""
Define text_identation functions
"""


def text_indentation(text):
    """Define indentation functions strings"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for caracters in ".:?":
        text = (caracters + "\n\n").join(
            [line.strip(" ") for line in text.split(caracters)])

    print("{}".format(text), end="")
