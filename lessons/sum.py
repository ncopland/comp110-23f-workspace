"""Summing the elements of a list using different loops."""


__author__ = "730659660"


def w_sum(vals: list[float]) -> float:
    """Sums using a while loop."""
    sum: float = 0

    x = 0
    while x < len(vals):
        sum += vals[x]
        x += 1

    return sum


def f_sum(vals: list[float]) -> float:
    """Sums using a for in loop."""
    sum: float = 0

    for item in vals:
        sum += item

    return sum


def f_range_sum(vals: list[float]) -> float:
    """Sums using a for range loop."""
    sum: float = 0

    for item in range(0, len(vals)):
        sum += vals[item]

    return sum
