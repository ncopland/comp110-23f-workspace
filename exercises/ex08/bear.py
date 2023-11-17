"""File to define Bear class."""


class Bear:
    """Creates the bear class."""
    
    def __init__(self, age: int = 0, hunger_score: int = 0):
        """Constructor."""
        self.age = age
        self.hunger_score = hunger_score
        return None
    
    def one_day(self):
        """Sim one day for bear."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Eat function to control hunger score."""
        self.hunger_score += num_fish
        return None