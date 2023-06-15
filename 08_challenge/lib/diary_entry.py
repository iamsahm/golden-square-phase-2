# File: lib/diary_entry.py

class DiaryEntry:
    def __init__(self, title, contents):
        if type(title) != str or type(contents) != str:
            raise Exception("Diary arg should not be int.")
        self.title = title
        self.contents = contents
        self.content_list = self.contents.split()
        self.bookmark = 0

    def format(self):
        return f"{self.title}: {self.contents}"
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"

    def count_words(self):
        return len(self.content_list)

    def reading_time(self, wpm):
        if type(wpm) != int:
            raise Exception("wpm needs to be an int")
        return self.count_words() / wpm 

        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.

    def reading_chunk(self, wpm, minutes):
        total_words_read = wpm * minutes
        words_we_have_to_read = self.content_list[self.bookmark:]
        words_we_are_reading = words_we_have_to_read[:total_words_read]
        joint_string = " ".join(words_we_are_reading)
        self.bookmark = len(words_we_are_reading) % len(self.content_list)
        if total_words_read > len(words_we_have_to_read):
            wordsplurge = total_words_read - len(words_we_have_to_read)
            print (f'{wordsplurge} should be {40*4}')

            result = joint_string + ' ' + ' '.join(self.content_list[:wordsplurge])
            print (result.split())
            print (("you also the contents "*60 + 'i am the contents '*40).split())
            return result
        return joint_string



        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass


'''
class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        pass'''