"""Summing the elements of a list using different loops."""

from __future__ import annotations


__author__ = "730659660"


class Point:
    """Point class."""

    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutating method that mutates point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creates a new point."""
        return Point(self.x * factor, self.y * factor)

    def __str__(self) -> str:
        """Prints out appealing point format."""
        output = f"x: {self.x}; y: {self.y}"
        return output
    
    def __mul__(self, factor: int | float) -> Point:
        """Multiplication operator overload."""
        new: Point = Point(self.x * factor, self.y * factor)
        return new

    def __add__(self, factor: int | float) -> Point:
        """Adds to existing point."""
        new: Point = Point(self.x + factor, self.y + factor)
        return new