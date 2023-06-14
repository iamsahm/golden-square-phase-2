class DiaryEntry:
    
    def __init__(self, title, contents):
        pass

    def count_words(self):
        pass


class Diary:
    
    def __init__(self):
        self.phone_numbers = []

    def add(self, entry: DiaryEntry) -> None:
        # parse through text - find phone numbers
        # add to self.phone
        pass

    def find_best_diary_for_time(self, wpm: int, minutes: int) -> DiaryEntry:
        pass

    def read_all(self) -> list[DiaryEntry]:
        pass


diary = Diary()
diary.find_best_diary_for_time("hhkkjh", "jgjhjh")