# When we add entry, we get the title and contents back in the diary object
from lib.diary import *

# initially no entries

def test_diary_starts_empty():
    my_diary = Diary()
    assert my_diary.entries == []
    
