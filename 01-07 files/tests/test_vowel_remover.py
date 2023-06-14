# File: tests/test_vowel_remover.py

from lib.vowel_remover import *

def test_simple():
    remover = VowelRemover("ab")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "b"

def test_long_sentence_with_punctuation():
    remover = VowelRemover("We will remove the vowels from this sentence.")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "W wll rmv th vwls frm ths sntnc."


# A colleague has done a code review and has advised that the tests should 
# cover all the vowels.

# Add a new unit test to 
def test_program_removes_vowels_from_aeiou():
    remover = VowelRemover('aeiou')
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == ''
# check that the program can remove all the vowels from "aeiou",
# returning an empty string, "". 
# If there are any problems reported by pytest after adding this new test, use
#  the debugger to look into vowel_remover.py to discover where the problem is and make any necessary changes.

# If you're having trouble or aren't sure what to do and want to watch us running through the exercise 
# using the debugger, here's our accompanying video covering this vowel-removing exercise, where we also
#  use Watch on things like self.text[:i] to gain even more visibility