# When we add entry, we get the title and contents back in the diary object
from lib.diary import *
from lib.diary_entry import *

def test_diary_accepts_entry():
    my_diary = Diary()
    entry_1 = DiaryEntry('Monday', 'Slay')
    entry_2 = DiaryEntry('Tuesday', 'send me back to the weekend please')
    my_diary.add(entry_1)
    my_diary.add(entry_2)
    assert my_diary.all() == [entry_1, entry_2]


# When we add entries count_words returns an integer representing the number of words in all the contents
def test_diary_count_returns_total_contents_integer():
    my_diary = Diary()
    my_diary.add(DiaryEntry('Monday', 'slay'))
    my_diary.add(DiaryEntry('Tuesday', 'send me back to the weekend please'))
    my_diary.add(DiaryEntry('Wednesday', 'it isn\'t so bad maybe we will be ok'))
    my_diary.add(DiaryEntry('Thursday', 'pint later?'))
    assert my_diary.count_words() == 19


# When we add entries, reading_time returns an integer representing an estimate of the reading time of the contents at the given wpm
def test_reading_time_returns_time_to_read_all_entries():
    my_diary = Diary()
    my_diary.add(f'Monday, {"slay"*100}')
    my_diary.add(f'Tuesday, {"send me back to weekend"*20}')
    my_diary.add(f'Wednesday {"it isn't so bad maybe we will be ok no"*10}')
    assert my_diary.reading_time(30) == 10
'''
# When we add entries, all() returns a list of Diary instances
def test_diary_add_entries_then_all_returns_list_of_entries():
    my_diary = Diary()
    my_diary.add(DiaryEntry('Monday', 'slay'))
    my_diary.add(DiaryEntry('Tuesday', 'send me back to the weekend please'))
    my_diary.add(DiaryEntry('Wednesday', 'it isn\'t so bad maybe we will be ok'))
    my_diary.add(DiaryEntry('Thursday', 'pint later?'))
    assert my_diary.all() == [['Monday', 'slay'],['Tuesday', 'send me back to the weekend please'],['Wednesday', 'it isn\'t so bad maybe we will be ok'],['Thursday', 'pint later?']]


# When we add entries, find_best_entry_for_reading_time returns an instance of DiaryEntry that is closest (but not over) the length the user could read in the minutes at the wpm given
my_diary = Diary()
my_diary.add(Monday: f'{"slay"*80}')
my_diary.add(Tuesday: f'{"send me back to weekend"*20}')
my_diary.add(Wednesday: f'{"it isn't so bad maybe we will be ok no"*10}')
my_diary.find_best_entry_for_reading_time(30, 3) == str(Monday: f'{"slay"*80}')

'''