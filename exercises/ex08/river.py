"""File to define River class."""

__author__ = "730659660"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """River Class."""
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes old animals."""
        new_fish: list = []
        new_bears: list = []
        for item in self.fish:
            if item.age > 3:
                item = item
            else:
                new_fish.append(item)

        for item in self.bears:
            if item.age > 5:
                item = item
            else:
                new_bears.append(item)

        self.fish = new_fish
        self.bears = new_bears
        return None
    
    def remove_fish(self, amount: int):
        """Removes x fish."""
        for x in range(0, amount):
            self.fish.pop(x)

    def bears_eating(self):
        """Models bears eating fish."""
        for item in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                item.eat(3)
            else:
                self.bears.pop(-1)
        return None
    
    def check_hunger(self):
        """Kills starving bears."""
        new_bears: list = []
        for x in range(0, len(self.bears)):
            if self.bears[x].hunger_score < 0:
                x = x
            else:
                new_bears.append(self.bears[x])

        self.bears = new_bears
                
        return None
        
    def repopulate_fish(self):
        """Reproduction of fish modeled."""
        x = 0
        while x < len(self.fish) // 2 - 1:
            for x in range(0, 3):
                self.fish.append(Fish())
            x += 1

        return None
    
    def repopulate_bears(self):
        """Reproduction of bears modeled."""
        x = 0
        while x < len(self.bears) // 2:
            self.bears.append(Bear())
            x += 1

        return None
    
    def view_river(self):
        """Prints out the day and populatoins."""
        output = f"~~~ Day {self.day}: ~~~\n"
        output += f"Fish population: {len(self.fish)}\n"
        output += f"Bear population: {len(self.bears)}\n"
        print(output)
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates the week 7 times."""
        for x in range(1, 8):
            self.one_river_day()