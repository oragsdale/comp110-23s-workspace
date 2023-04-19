"""File to define River class."""

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

class River:
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def remove_fish(self, amount: int):
        for x in range(amount):
            self.fish.pop(x)
        return None

    def bears_eating(self):
        for bears in self.bears:
            if len(self.fish) > 4: 
                self.remove_fish(3)
                bears.eat(3)
        return None
    
    def check_hunger(self):
        bears: list[Bear] = []
        for x in self.bears:
            if x.hunger_score() >= 0:
                bears.append(x)
        self.bears = bears

        return None
                
    def check_ages(self):
        fish : list[Fish] = []
        for x in self.fish:
            if x <= 3: 
                fish.append(x)
        self.fish = fish

        bears: list[Bear] = []
        for x in self.bears:
            if x <= 5:
                bears.append(x)
        self.bears = bears

        return None
        
    def repopulate_fish(self):
        num_fish: int = len(self.fish)
        self.bears += (num_fish//2) * 4
        return None
    
    def repopulate_bears(self):
        num_bears: int = len(self.bears)
        self.bears += num_bears//2

        return None
    
    def view_river(self):
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
        while self.day < 7:
            self.one_river_day()
