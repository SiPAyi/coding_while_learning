# Here if the condition is true, if block
# will consider only statement1 to be inside
# its block
i = 10
if (i> 15):
    print ("10 is less than 15")
    print ("I am Not in if")


# if (condition1):
#    Executes when condition1 is true
#   if (condition2):
#       Executes when condition2 is true
#       if Block is end here
#   if Block is end here
i = 20;
if (i< 15):
    print ("i is smaller than 15")
    print ("i'm in if Block")
else:
    print ("i is greater than 15")
    print ("i'm in else Block")
    print ("i'm not in if and not in else Block")


# if (condition):
# statement
# elif (condition):
# statement
# else:
# statement
i = 20
if (i == 10):
    print ("i is 10")
elif (i == 15):
    print ("i is 15")
elif (i == 20):
    print ("i is 20")
else:
    print ("i is not present")


# Python program to illustrate short hand if i = 10
if i< 15: print("i is less than 15")


# Python program to illustrate short hand if-else i = 10
print(True) if i< 15 else print(False)