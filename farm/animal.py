"""
Module: animal
Defines the base Animal class.
"""


class Animal:
    """Base class for all farm animals."""

    def __init__(self):
        """Initialize the animal with zero energy."""
        self.energy = 0

    def feed(self):
        """Feed the animal and increase its energy by 1."""
        self.energy += 1
