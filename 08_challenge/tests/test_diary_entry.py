from lib.diary_entry import *
import pytest

#test init
def test_diary_entry_init():
    diary = DiaryEntry("hello", "diary contents")
    assert type(diary) == DiaryEntry

#raise error if contents or diary not str
def test_diary_entry_contents_not_str_raises_error():
    with pytest.raises(Exception) as e:
        DiaryEntry("Hello", 90)
    error_message = str(e.value)
    assert error_message == "Diary arg should not be int."

def test_diary_entry_title_not_str_raises_error():
    with pytest.raises(Exception) as e:
        DiaryEntry(89, "goodbye")
    error_message = str(e.value)
    assert error_message == "Diary arg should not be int."

#test self.format returns formatted title and contents
def test_diary_entry_returns_formatted_title_and_contents():
    diary = DiaryEntry("Hello", "i am the contents")
    assert diary.format() == "Hello: i am the contents"

#count words returns number of words in diary entry as int
def test_diary_entry_returns_num_words_as_int():
    diary = DiaryEntry("Hello", "i am the contents")
    assert diary.count_words() == 4

#reading time returns int in minutes for contents at given wpm
def test_diary_entry_reading_time_returns_int_in_minutes():
    diary = DiaryEntry("Hello", "i am the contents "*100)
    assert diary.reading_time(40) == 10 

#reading time raise error if wpm is not int
def test_diary_entry_raises_error_if_wpm_not_int():
    diary = DiaryEntry("Hello", "i am the contents "*100)
    with pytest.raises(Exception) as e:
        diary.reading_time("90")
    error_message = str(e.value)
    assert error_message == "wpm needs to be an int"

#reading chunk returns a chunk of the contents that the user could read in the given number of minutes
#added minutes parameter
def test_diary_entry_reading_chunks_returns_contents_user_can_read_in_given_time():
    diary = DiaryEntry("Hello", "i am the contents "*100)
    result = diary.reading_chunk(40, 6)
    result_var = "i am the contents "*60
    assert result == result_var[:-1]


#reading chunk called twice returns seperate chunks
def test_diary_entry_chunk_twice_seperate_chunk():
    diary = DiaryEntry("Hello", "i am the contents "*40 + 'you am also the contents '*60)
    diary.reading_chunk(40,4)
    result = diary.reading_chunk(40,4)
    result_var = "you am also the contents "*32
    assert result == result_var[0:-1]
    
#reading chunk raise error if wpm or minutes not int

#if reading chunk gets to the end lops back to the beginning
def test_diary_entry_long_chunk_twice_seperate_chunk():
    diary = DiaryEntry("Hello", "i am the contents "*40 + 'you also the contents '*60)
    diary.reading_chunk(40,4)
    result = diary.reading_chunk(40,10)
    result_var = 'you also the contents '*60 + 'i am the contents '*40
    assert result == result_var[0:-1]