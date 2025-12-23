"""
Module: chicken
Defines the Chicken class.
"""

from farm.animal import Animal


class Chicken(Animal):
    """Chicken animal."""
    def __init__(self,gender):
        """Initialize a chicken with its sex."""
        super().__init__()
        self.gender = gender
        self.eggs = 0

    def talk(self):
        """Return the sound a chicken makes based on its sex."""
        if self.gender == "female":
            return "cluck cluck"
        return "cock-a-doodle-doo"
    def feed(self):
        super().feed()
        if self.gender == "female":
            self.eggs += 2
