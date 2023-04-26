"""File to define Fish class."""


class Fish:
    """Fish defines the age and aging process for the fish in the river."""

    age: int

    def __init__(self):
        """Initializes age."""
        self.age = 0

    def one_day(self):
        """Adds to the fish's age after one day."""
        self.age += 1
        return None