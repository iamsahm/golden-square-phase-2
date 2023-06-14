# #Design

# A function called make_snippet that takes a string as an argument and returns the first 
# five words and then a '...' if there are more than that. 

# Write a small example as a test.
# # Run the test (RED).
# Write enough code to make that test pass.
# Run the test (GREEN).
# Refactor if necessary.
# Return to step 1 and keep going until your program is complete.

from lib.make_snippet import *

def test_longstring():
    result = make_snippet('help me obi wan you are my only hope')
    assert result == 'help me obi wan you...'
def test_shortstring():
    result = make_snippet('got milk?')
    assert result == 'got milk?'
def test_five_words():
    result = make_snippet('here are five short words')
    assert result == 'here are five short words'