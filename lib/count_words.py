def count_words(string):
    number = 0

    stringlist = string.split()
    for i in stringlist:
        if i.isalpha():
            number += 1 
    return number


