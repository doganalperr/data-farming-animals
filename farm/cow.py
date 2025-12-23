"""
Module: cow
Defines the Cow class.
"""

from farm.animal import Animal

class Cow(Animal):
    """Cow animal."""
    def __init__(self):
        super().__init__()
        self.milk = 0

    def talk(self):
        """Return the sound a cow makes."""
        return "moo"

    def feed(self):
        super().feed()
        self.milk += 2
