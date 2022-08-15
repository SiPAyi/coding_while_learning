# Write a program to check the given string is palindrome or not?

word = input('enter a string : ')

if word == word[::-1]:
    print(word, 'is a polindrom')
else:
    print(word, 'is not a polindrom')