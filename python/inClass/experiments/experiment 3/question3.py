# Write a program to find the no.of words, no.of vowels, no.of capital alphabets,
# no.of small alphabets, no.of digits, no of spaces and no.of special characters from the
# given string
# s=” I am learning Python Programming Language from 2 months. There are 35
# reserved keywords in Python 3.9 version.and some operators line +,%,-,&& and etc.”


string = input('enter your string : ')

alpha = 0
words = 0
vowels = 0
caps = 0
lowers = 0
digits = 0
spaces = 0
specials = 0

for letter in string:
    if letter.isalpha():
        alpha += 1
        if letter.islower():
            lowers += 1
        elif letter.isupper():
            caps += 1
        if letter in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
    elif letter.isdigit():
        digits += 1
    elif letter.isspace():
        spaces += 1
        words += 1
    else:
        specials += 1

print('alphabets', alpha)
print('capital letters', caps)
print('lower alphabets', lowers)
print('vowels', vowels)
print('digits', digits)
print('spaces', spaces)
print('words', words+1)
print("special characters", specials)
