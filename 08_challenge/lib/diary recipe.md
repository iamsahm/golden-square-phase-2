# When we add entry, we get the title and contents back in the diary object
my_diary = Diary()
my_diary.add(Monday: slay)
my_diary.contents == slay
my_diary.entries == ['Monday', 'slay']

# When we add entries count_words returns an integer representing the number of words in all the contents
my_diary = Diary()
my_diary.add(Monday: slay)
my_diary.add(Tuesday: send me back to the weekend please)
my_diary.add(Wednesday: it isn't so bad maybe we will be ok)
my_diary.add(Thursday: pint later?)
my_diary.count_words() == 19

# When we add entries, all() returns a list of Diary instances
my_diary = Diary()
my_diary.add(Monday: slay)
my_diary.add(Tuesday: send me back to the weekend please)
my_diary.add(Wednesday: it isn't so bad maybe we will be ok)
my_diary.add(Thursday: pint later?)
my_diary.all() == [['Monday', 'slay'],['Tuesday', 'send me back to the weekend please'],['Wednesday', 'it isn't so bad maybe we will be ok'],['Thursday', 'pint later?']]

# When we add entries, reading_time returns an integer representing an estimate of the reading time of the contents at the given wpm
my_diary = Diary()
my_diary.add(Monday: f'{"slay"*100}')
my_diary.add(Tuesday: f'{"send me back to weekend"*20}')
my_diary.add(Wednesday: f'{"it isn't so bad maybe we will be ok no"*10}')
my_diary.reading_time(30) == 10

# When we add entries, find_best_entry_for_reading_time returns an instance of DiaryEntry that is closest (but not over) the length the user could read in the minutes at the wpm given
my_diary = Diary()
my_diary.add(Monday: f'{"slay"*80}')
my_diary.add(Tuesday: f'{"send me back to weekend"*20}')
my_diary.add(Wednesday: f'{"it isn't so bad maybe we will be ok no"*10}')
my_diary.find_best_entry_for_reading_time(30, 3) == str(Monday: f'{"slay"*80}')

# DIARY_ENTRY SPECIFIC TESTS:
# # When we call reading chunk twice, it should return the next chunk until the contents is read
<!-- these tests were written in a previous chapter, i've copied them in here but we might need to update them to reflect changes in this challenge -->
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

# When we call reading chunk after the contents is all read, the next reading chunk call starts from the beginning of the contents
