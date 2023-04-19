"""File to define Bear class."""


class Bear:
    """Bear defines the age, hunger_score, and eating caculations for the bears in the river."""    

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes age and hunger_score."""
        self.age = 0
        self.hunger_score = 0
    
    def one_day(self):
        """Asseses updates to age and hunger_score after one day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Changes hunger_score when the bears eat."""
        self.hunger_score += num_fish
        return None