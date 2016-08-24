#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""

:mod:`lab_pyreview` -- Python review
=========================================

LAB PyReview Learning Objective: Review the topics from the previous courses

a. Load the data from the two dictionary files in the data directory into two
   list objects.  data/dictionary1.txt data/dictionary2.txt
   Print the number of entries in each list of words.

b. Use sets in Python to merge the two lists of words with no duplications
   (union). Print the number of words in the combined list.

c. Import the random library and use one of the functions to print out five
   random words from the combined list of words.

d. Use a list comprehension to find all the words that start with the letter
   'a'. Print the number of words that begin with the letter 'a'.

e. Create a function called wordcount() with a yield that takes the list of
   all words as an argument and yields a tuple of
   (letter, number_of_words_starting_with_that_letter) with each iteration.

"""

from random import sample
from string import lowercase

FILE_A = "../data/dictionary1.txt"
FILE_B = "../data/dictionary2.txt"


def wordcount(words):
    """
    all words as an argument and yields a tuple of
    (letter, number_of_words_starting_with_that_letter) with each iteration.

    Note: Assumes all input is lowercase
    :param words: a list of all words
    :return:
    """
    for letter in lowercase:
        yield (letter, len([word
                            for word in words
                            if word[0] == letter]))


def main():

    with open(FILE_A, "r") as infile:
        file_a_list = infile.read().splitlines()

    with open(FILE_B, "r") as infile:
        file_b_list = infile.read().splitlines()

    print("The number of entries in file A is %s" % len(file_a_list))
    print("The number of entries in file B is %s" % len(file_b_list))
    print

    union = set(file_a_list) | set(file_b_list)

    print("The number of entries in union of both files is %s" % len(union))
    print

    print(
        "Here are 5 random selections from the union:\n\t%s" %
        ', '.join([elem
                   for elem in [
                       sample(union, 1)[0] for _ in range(5)
                       ]
                   ]
                  )
    )
    print

    print(
        "The number of words that start with the letter 'a' is: %s" %
        len([elem for elem in union if elem[0] == 'a'])
    )
    print

    print(
        "Excercising the wordcount function:\n%s" %
        '\n'.join("%s: %s" % (word[0], word[1]) for word in wordcount(union))
    )


if __name__ == '__main__':
    main()
