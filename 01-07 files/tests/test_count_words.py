# Design

# A function called count_words that takes a string as an argument and returns the number of words in that string.
from lib.count_words import *
# Test a string with lots of words
def test_lots_of_words():
    result = count_words('here are lots of words')
    assert result == 5

# test a string with one word
def test_one_word():
    result = count_words('one')
    assert result == 1

# test a string with no words
def test_no_words():
    result = count_words('1 4 ?"**')
    assert result == 0
# test an empty string
def test_empty_string():
    result = count_words('')
    assert result == 0
