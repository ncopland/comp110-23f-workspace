"""File to define Fish class."""


class Fish:
    """Creates the fish class."""

    def __init__(self, age: int = 0):
        """Constructor with age."""
        self.age = age
        return None
    
    def one_day(self):
        """Adds age per day for a fish."""
        self.age += 1
        return None