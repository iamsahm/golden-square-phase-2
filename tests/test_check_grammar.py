from lib.grammarstats import *
import pytest

#returns False with non-str input 
def test_check_grammar_returns_false_no_input():
    grammarstats = GrammarStats()
    result = grammarstats.check(90)
    assert result == False
#returns False with a lower case start letter
def test_check_grammar_returns_false_for_lowercase():
    grammarstats = GrammarStats()
    result = grammarstats.check("hello there!")
    assert result == False
#returns False with non-sentance ending punctuation mark
def test_check_grammar_no_punctuation_returns_false():
    grammarstats = GrammarStats()
    result = grammarstats.check("Hello there()")
    assert result ==  False

#else returns True
def test_check_grammar_returns_true():
    grammarstats = GrammarStats()
    result = grammarstats.check("Hello there.")
    assert result ==  True

# returns percentage of texts so far that pass the check
def test_quarter_good_returns_25():
    grammarstats = GrammarStats()
    grammarstats.check("Hello there.")
    grammarstats.check("Hello there()")
    grammarstats.check("hello there!")
    grammarstats.check("hello there")
    result = grammarstats.percentage_good()
    assert result ==  25

# returns no percentage when no tests check
def test_percentage_good_non_returns_zero():
    grammarstats = GrammarStats()
    grammarstats.check("Hello there")
    grammarstats.check("Hello there()")
    grammarstats.check("hello there!")
    grammarstats.check("hello there")
    result = grammarstats.percentage_good()
    assert result ==  0

# returns exception message when no tests have been made
def test_percentage_good_no_tests_raises_error():
    with pytest.raises(Exception) as e:
        grammarstats = GrammarStats()
        grammarstats.percentage_good()
    assert str(e.value) == 'Make a test to return a percentage success!'
