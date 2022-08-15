# Write a Python program which iterates the integers from 1 to 50. For multiples of
# three print "RKV"
# " instead of the number and for the multiples of seven print "
# "ONG".
# For numbers which are multiples of both three and seven print "RKVONG"

for i in range(1, 51):
    if i % 3 == 0:
        print("RKV")
    elif i % 7 == 0:
        print("ONG")
    elif i % 3 == 0 and i % 7 == 0:
        print("RKVONG")
    else:
        print(i)