"""File to define River class."""

__author__ = "730560351"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

from fish import Fish
from bear import Bear

class River:
    """Enacts multiple processes between the bears and fish within the river."""
    
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

    def bears_eating(self):
        """Removes fish and changes bears' hunger scores when the bears eat."""
        for bears in self.bears:
            if len(self.fish) > 4: 
                self.remove_fish(3)
                bears.eat(3)
        return None
    
    def check_hunger(self):
        return None
                
    def check_ages(self):
        return None
        
    def repopulate_fish(self):
        """Adds to the fish population given the number of fish that were born."""
        num_fish: float = len(self.fish)
        for x in range(num_fish // 2 * 4):
            self.fish.append(x)
        return None
    
    def repopulate_bears(self):
        """Adds to the number of bears given the number of bears that were born."""
        num_bears: float = len(self.bears)
        for x in range(num_bears // 2):
            self.bears.append(x)
        return None
    
    def view_river(self):
        """Displays the number of fish and bears in the river."""
        print(f"~~~ Day {self.day}: ~~~\nFish population: {len(self.fish)}\nBear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
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
        """Runs one_river_day 7 times in order to create a full week."""
        while self.day < 7:
            self.one_river_day()