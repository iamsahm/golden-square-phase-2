import re

class DiaryEntry:
    
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        pass

    def count_words(self):
        return len(self.contents.split(' '))


class Diary:
    
    def __init__(self):
        self.phone_numbers = []
        self.entries = []

    def add(self, entry: DiaryEntry) -> DiaryEntry:
        # parse through text - find phone numbers
        # add to self.phone
        self.entries.append(entry)
        return entry

    def find_best_diary_for_time(self, wpm: int, minutes: int) -> DiaryEntry:
        best_entry = None
        total_words_read = wpm*minutes
        
        for entry in self.entries:
            word_count = entry.count_words()
            if word_count <= total_words_read:
                if best_entry is None or best_entry.count_words()<word_count:
                    best_entry = entry
        return best_entry


    def read_all(self) -> list[DiaryEntry]:
        return self.entries
    
    def get_phone_numbers(self):
        results = []
        for entry in self.entries:
            re_results = re.findall(r"\b\d{5}\s\d{6}\b", entry.contents)
            print (re_results)
            for i in re_results:
                results.append(i)
        return results
        
