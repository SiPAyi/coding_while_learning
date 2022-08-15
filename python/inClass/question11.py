# Write a program to accept a number from 1 to 7 and display the name of the day like 1 for
# Sunday , 2 for Monday and so on

day = int(input('enter the day number : '))

if day == 1:
    print('monday')
elif day == 2:
    print('tuesday')
elif day == 3:
    print('wednesday')
elif day == 4:
    print('thusday')
elif day == 5:
    print('friday')
elif day == 6:
    print('saturday')
elif day == 7:
    print('sonday')
else :
    print('Invalid input !!')


# another way of doing this


# days = ['monday','tuesday','wednesday','thusday','friday','saturday','sunday','invalid input']

# if 1 < day < 7:
#     print(days[day-1])
# else:
#     print(days[-1])