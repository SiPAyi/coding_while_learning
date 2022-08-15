# Given a list of tuples. Write a program to filter all uppercase characters tuples from
# given list of tuples. (Hint: Use Loop)
#  Input:test_list = [("GFG", "IS", "BEST"), ("GFg", "AVERAGE"), ("GfG", ), ("Gfg", "CS")],
#  Output : [("GFG", "IS", "BEST")]

from curses.ascii import isalnum, islower


test_list = [("GFG", "IS", "BEST"), ("GFg", "AVERAGE"),('KOO'), ("GfG", ), ("Gfg", "CS")]

all_upper_case_letters = []
for words_tuple in test_list:
    words = words_tuple
    for word in words_tuple:
        for letter in word:
            if letter.isupper():
                word = 'all uppercase'
            else:
                word = 'not uppercase'
                break

        if word == 'all uppercase':
            words = 'all words contains uppercases letters'
        else:
            words = 'not all words contain upper case letters'
            break
    all_upper_case_letters.append((words_tuple, words))

print(all_upper_case_letters)
