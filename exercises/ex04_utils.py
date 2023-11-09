"""EX04 - Lists."""

__author__ = "730659660"


def all(numbers: list[int], target: int) -> bool:
    """Checks that a list is all the same as a target number."""
    index = 0
    if (len(numbers) == 0):
        return False
    while (index < len(numbers)):
        num = numbers[index]
        if num != target:
            return False
        index += 1
    return True


def max(input: list[int]) -> int:
    """Finds the max in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max = input[0]
    index = 0
    while (index < len(input)):
        num = input[index]
        if num > max:
            max = num
        index += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if two lists are equal."""
    index = 0
    if len(list1) != len(list2):
        return False
    while (index < len(list1)):
        if list1[index] != list2[index]:
            return False
        index += 1
    return True
