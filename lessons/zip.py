"""Combining two lists into a dictionary."""

__author__ = "730659660"


def zip(a: list[str], b: list[int]) -> dict[str, int]:
    """Function to create a dictionary between two lists."""
    dictionary: dict[str, int] = {}
    if len(a) != len(b):
        return dictionary
    else:
        x = 0
        for item in a:
            dictionary[item] = b[x]
            x += 1

        return dictionary