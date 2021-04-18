"""
Gannon Leech
CSCI 3725: Computational Creativity
Last Modified: 4/17/21
Description: This class creates the Poem object. It is a very simple class
that only has attributes for its own fitness, and for the first and second
half, which made it easier to do crossover.
Known Bugs: There are no known bugs
"""


class Poem:
    def __init__(self):
        """
            Poem class, fairly basic, has attributes for the first and second
            halves in order to make crossbreeding simpler, and then an
            attribute to record the fitness for each poem.
        """
        self.first_half = ""
        self.second_half = ""
        self.fitness = 0

    def __str__(self):
        """ Provides a string representation of the poem, with the first and
        second half connected"""
        return str(self.first_half + self.second_half)

    def __repr__(self):
        """ Provides a representation of the poem, with the first and second
        half connected"""
        return str(self.first_half + self.second_half)
