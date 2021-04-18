"""
Gannon Leech
CSCI 3725: Computational Creativity
Last Modified: 4/17/21
Description: This class sets up the WordDictionary, which stores
sequences of words in a dictionary where the values for those
sequences are additional dictionaries containing the words that
follow those sequences and their occurences. This is used to help
set up the n-gram model
Known Bugs: There are no known bugs
"""


class wordDictionary:
    def __init__(self):
        """
            A class whose only attribute is a dictionary which stores
            sequences of words with a dictionary containing their
            occurences
        """
        self.dictionary = dict()

    def add_dict(self, new_dict, word):
        """
            Addss a given file dictionary to the overall word dictionary

            new_dict (fileDictionary): a file dictionary that is being added
            to the overall word dictionary
            word (string): the word that is being referenced in the
            fileDictionary
        """
        if new_dict.sequence in self.dictionary.keys():
            self.dictionary[new_dict.sequence].update_dict(word)
        else:
            self.dictionary[new_dict.sequence] = new_dict

    def get_next_word(self, sequence, random_word):
        """
            Based on a given sequence of words, probabilistically
            returns the next word

            sequence (string): the preceding sequence of words
            random_word (string): a random word to use in case
            the sequence does not appear in the n gram model
        """
        total = 0
        if sequence in self.dictionary.keys():
            total = self.dictionary[sequence].get_count_sum()
            return self.dictionary[sequence].next_word(total)
        else:
            return random_word + " "

    def __str__(self):
        """
            returns a string representation of the wordDictionary
        """
        return str(self.dictionary)

    def __repr__(self):
        """
            returns a string representation of the wordDictionary
        """
        return str(self.dictionary)
