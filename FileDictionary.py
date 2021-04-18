"""
Gannon Leech
CSCI 3725: Computational Creativity
Last Modified: 4/17/21
Description: This class sets up the FileDictionary, which is a dictionary
that stores the word that follows the corresponding sequence for the
fileDictionary and the number of occurences for that word, which is
used to set up the n-grams model
Known Bugs: There are no known bugs
"""

import random as rand


class fileDictionary:
    def __init__(self, sequence):
        """
            Initalizes a fileDictionary, which requires a sequence of
            words based on the inputted n value, and then stores the
            occurences of the words that follow that sequence
        """
        self.sequence = sequence
        self.fileDict = dict()

    def get_sequence(self):
        """
            returns the sequence for a given fileDictionary
        """
        return self.sequence

    def update_dict(self, word):
        """
            updates the dictionary by incrementing the number of occurences
            of the given word

            word (string): the word whose number of occurences is to be
            incremented
        """
        if word in self.fileDict.keys():
            self.fileDict[word] = self.fileDict[word] + 1
        else:
            self.fileDict[word] = 1

    def get_count_sum(self):
        """
            returns the total number of occurences for a single
            sequence
        """
        val_sum = 0
        for key in self.fileDict.keys():
            val_sum += self.fileDict[key]

        return val_sum

    def next_word(self, total):
        """
            probabilistically selects what the next word should
            be after a sequence

            total (int): the total number occurences of a
            given sequence
        """
        val_sum = 0
        random_val = rand.randint(0, total - 1)
        current_word = ''

        for key in self.fileDict.keys():
            val_sum += self.fileDict[key]
            if val_sum >= random_val:
                return key

        return current_word

    def __str__(self):
        """
            Returns a string representation for the FileDictionary
        """
        return str(self.fileDict)

    def __repr__(self):
        """
            returns a string representation for the FileDictioanry
        """
        return str(self.fileDict)
