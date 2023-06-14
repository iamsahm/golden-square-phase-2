from lib.letter_counter import *

def test_letter_counter():

    counter = LetterCounter("Digital Punk")
    assert (counter.calculate_most_common()) == [2, 'i']
# Intended output:
# [2, "i"]