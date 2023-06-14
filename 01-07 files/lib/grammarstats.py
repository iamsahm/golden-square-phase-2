class GrammarStats():
    def __init__(self):
        self.good_counter = 0
        self.counter = 0
        pass
  
    def check(self, text):
        # Parameters:
        #   text: string
        self.counter +=1
        if type(text) != str:
            return False
        is_lower = text[0].isupper()
        is_punctuation = text[-1] in "!?."

        if is_lower and is_punctuation:
            self.good_counter += 1
            return True
        else:
            return False

        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        
    def percentage_good(self):
        # Returns:
        if self.counter == 0:
            raise Exception('Make a test to return a percentage success!')
        return self.good_counter/self.counter*100
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.