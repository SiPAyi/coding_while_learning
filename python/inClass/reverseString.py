def reverse(word):
    newString = ""
    for i in range(len(word)):
        newString += word[len(word)-i-1]
    return newStringfrom stringMethods import reverse

string = input('enter a string : ')

print(reverse(string))