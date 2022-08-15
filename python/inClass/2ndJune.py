## split method
# s = 'rgukt is an university for technial education'
# s = 'sai'

# k = s.split()

# print(k)

# jointed = '*'.join(k)
# print(jointed)


##strip
# a = '***rgukt*'
# # a = input('enter input : ')

# print(a.strip('*'))

## to get the ascii value of a letter
# print(ord('d'))


# # to get the letter by it's ascii value
# print(chr(122))

# for i in range(1,127):
#     print(i, '=', chr(i), end=',  ')
# print()


## write a program to reverse a string
# word = input('enter the string : ')
# reversed = ''
# for i in range(len(word)-1,-1,-1):
#     reversed += word[i]
# print(reversed)

##write a program to check it is polyndrom or not
# word = input('enter the string : ')
# reversed = ''
# for i in range(len(word)-1,-1,-1):
#     reversed += word[i]
# if reversed == word:
#     print("it's a polyndrom bro!!")
# else:
#     print("it's not a polyndrom bro!!")


##find the length of the string without using the inbuild methods
# string = 'my name ... ._ ..'
# c = 0
# for i in string:
#     c += 1
# print(c)


## write a program to find number of letters, numbers, characters
# string = 'sai@2005'
# alpha = number = character = space = 0
# for i in string:
#     if i.isalpha():
#         alpha += 1
#     elif i.isdigit():
#         number += 1
#     elif i.isspace():
#         spaces += 1
#     else:
#         character += 1
# print(alpha, number, character, space)

##ASCII VALUES
# space --> 32
#characters --> 33 to 47 and 58 to 64 and 91 to 96 and 123 to 126
#numbers --> 48 to 57
#uppercase --> 65 to 90
#lowercase --> 97 to 122
