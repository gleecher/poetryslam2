"""
Gannon Leech
CSCI 3725: Computational Creativity
Last Modified: 4/17/21
Description: This is the main class for my poetry slam project.
This class contains most ofthe methods needed to run the program, including
the poetry generation functions, the functions to run the genetic algorithms,
and the functions to save out and speak the poem.
Known Bugs: There are no known bugs
"""


from FileDictionary import fileDictionary
from WordDictionary import wordDictionary
from poem import Poem
import random as rand
import datetime
from os import system


def main():
    filename = "inputs/"
    filename += input("Please enter the file to use as a template ")
    n_value = int(input("Please enter what value for n "))

    my_word = wordDictionary()
    first_line_checker = 0
    first_words = ""

    full_file = get_file_info(filename).strip('/n')
    words = full_file.split()

    for i in range(len(words) - n_value):
        sequence = ""
        if first_line_checker == 0:
            for k in range(n_value):
                first_words = first_words + words[i + k].lower() + " "
                first_line_checker += 1

        for j in range(n_value):
            word = words[i + j]
            word = word.lower()
            sequence = sequence + word + " "

        next_word = i + n_value
        my_dict = fileDictionary(sequence)
        my_dict.update_dict(words[next_word].lower())
        my_word.add_dict(my_dict, words[next_word].lower())

    population = seed_population(my_word, first_words)
    for generation in range(20):
        for poem in population:
            calc_fitness(poem, my_word)

        breeding_pool = select_breeding_pool(population)
        population = crossover(breeding_pool)

        # new_population = []
        # for poem in population:
        #    new_poem = mutate(poem, my_word, n_value)
        #    new_population.append(new_poem)

        # population = new_population

    best_poem = find_max(population)
    speak_poem(best_poem)
    write_out_poem(best_poem)


def find_max(population):
    """
        Returns the poem with the highest fitness from a given population

        population (list): a list of poem objects
    """
    best_poem = population[0]
    best_fitness = best_poem.fitness

    for poem in population:
        if poem.fitness > best_fitness:
            best_poem = poem
            best_fitness = poem.fitness

    return best_poem


def get_file_info(filename):
    """
        Uses the inputted filename to return the file as one long line to
        make it easier to parse for n-grams

        filename (string): the user inputted name of file to use as
        an inspiring set
    """

    full_file = ""
    file = open(filename, "r")
    for line in file.readlines():
        all_words = line.split()
        for word in all_words:
            full_file += word + " "
    file.close()
    return full_file


def select_breeding_pool(population):
    """
        Returns a list of poem objects which represents the breeding pool for
        a given generation. The breeding pool is selected from the current
        generation by randomly selecting two poems and then choosing the one
        that has the highest fitness until a population is generated equal to
        the original population

        population (list): a list of poem objects representing the current
        generation
    """
    breeding_pool = []
    for i in range(len(population)):
        vals = rand.sample(range(len(population)), 2)

        if population[vals[0]].fitness > population[vals[1]].fitness:
            breeding_pool.append(population[vals[0]])
        else:
            breeding_pool.append(population[vals[1]])

    return breeding_pool


def crossover(population):
    """
        Performs crossover on a given generation of poems, swapping the first
        and second halves of each poem in a generation

        population (list): A list representing the breeding pool for the
        current generation
    """
    new_population = []
    for i in range(0, len(population), 2):
        new_poem1 = Poem()
        new_poem1.first_half = population[i].first_half
        new_poem1.second_half = population[i + 1].second_half

        new_poem2 = Poem()
        new_poem2.first_half = population[i + 1].first_half
        new_poem2.second_half = population[i].second_half

        new_population.append(new_poem1)
        new_population.append(new_poem2)

    return new_population


def seed_population(my_word, first_words):
    """
        Generates a starting population of poems, using n-grams to generate
        a word based on a previous sequence of words

        my_word ()
        first_words (string): a string representing the first n words of
        the inspiring test, which are used to start the poem generation
    """
    poem_string = first_words
    old_sequence = first_words
    population = []

    # generates 20 poems for a generation
    for j in range(20):
        poem = Poem()

        # each poem is 50 words
        for i in range(50):
            if len(poem_string) == 0:
                random_word = old_sequence.split()[0]
            else:
                random_word = rand.choice(poem_string.split())
            new_word = my_word.get_next_word(old_sequence, random_word) + " "
            poem_string += new_word

            line_val = i % 10
            if line_val == 0:
                poem_string += '\n'

            if i == 25:
                poem.first_half = poem_string
                poem_string = ""
            if i == 49:
                poem.second_half = poem_string

            old_word_list = old_sequence.split()
            old_sequence = ""
            for k in range(1, len(old_word_list)):
                old_sequence = old_sequence + old_word_list[k] + " "
            old_sequence = old_sequence + new_word

        population.append(poem)

    return population


def calc_fitness(poem, word_dictionary):
    """
        calculates the fitness of an individual poem based on the variability
        of words and how realistic the poem is using the n grams

        poem (Poem): the poem to calculate the fitness of
        word_dictionary (word_dictionary): the word dictionary to help
        calculate how realistic the given poem is
    """
    overall_poem = poem.first_half + poem.second_half
    variability_score = calc_variability(overall_poem)
    likelihood_score = calc_likelihood(overall_poem, word_dictionary)
    poem.fitness = variability_score + likelihood_score


def calc_likelihood(poem, word_dictionary):
    """
        calculates the likelihood score for a poem based on how realistic the
        words are using the n grams model

        poem (Poem): the poem to measure
        word_dictionary (word_dictionary): the dictionary containing the
        n-gram information

    """
    likelihood_score = 0
    for word in poem.split():
        for key in word_dictionary.dictionary.keys():
            likelihood_score += \
                word_dictionary.dictionary[key].fileDict.get(word, 0)
    return likelihood_score


def calc_variability(poem):
    """
        calculates the variability of the poem based on the number of unique
        words within the poem

        poem (Poem): the poem to measure
    """
    words = poem.split()
    return len(set(words))


def mutate(poem, word_dictionary, n_value, mutation_prob=0.05):
    """
        Handles the mutation functions of the poem by calling helper functions

        poem(Poem): the given poem to mutate
        word_dictionary (word_dictionary): the dictionary containing the
         n-grams information
        n_value (int): the user inputted n value
        mutation_prob (float): the probability that an indivudal word would be
         mutated
    """
    new_poem = Poem()
    new_poem.first_half = get_words(poem.first_half, word_dictionary,
                                    n_value, mutation_prob)
    new_poem.second_half = get_words(poem.second_half, word_dictionary,
                                     n_value, mutation_prob)
    return new_poem


def get_words(poem_half, word_dictionary, n_value, mutation_prob):
    """
        Runs the mutation for a section of a poem by reselecting a word based
        on the n gram model with some small mutation probability

        poem_half(string): the given half of the poem to mutate
        word_dictionary (word_dictionary): the dictionary containing the
        n-grams information
        n_value (int): the user inputted n value
        mutation_prob (float): the probability that an indivudal word would
        be mutated
    """
    new_half = ""
    half_words = poem_half.split()

    for j in range(n_value):
        new_half += half_words[j] + " "

    for k in range(n_value - 1, len(half_words) - n_value):
        chance = rand.uniform(0, 1)
        if chance < mutation_prob:
            random_word = rand.choice(poem_half.split())
            sequence = ""
            for j in range(n_value):
                sequence += half_words[k + j]
            new_half += \
                word_dictionary.get_next_word(sequence, random_word) + " "
        else:
            new_half += half_words[k] + " "
        mod_val = k % 10
        if mod_val == 0:
            new_half += '\n'

    return new_half


def write_out_poem(poem):
    """Given a poem, writes it as a file in a designated results folder.
        poem(Recipe): Recipe being written to a .txt file
    """
    filename = ("outputs/Poem_" + str(datetime.datetime.now()))
    with open(filename, 'w+') as file:
        file.write(str(poem))


def speak_poem(poem):
    poem_lines = poem.first_half + poem.second_half
    command = "say " + str(poem_lines.strip())
    system(command)


if __name__ == "__main__":
    main()
