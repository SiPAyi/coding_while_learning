# write a program to check about curriculum of IIIT-ONG. We have generally 7 days in
# these Saturday is for exam and Sunday is a holiday except all days are
# Normal days, it means classes will go on according to periods.
# 1. If the entered day is Saturday then print 'Today is for exam' if the session is morning
# 2. and print 'Yahoo!!! it is time for movie' if the session is evening.
# 3.Just print 'It is all funnnnn!!!!' if the day is Sunday.
# 4.For Friday then print "This session is for classes" if the session is morning print
# 5."It is time for study hours” if the session is afternoon.
# 6.For remaining days just print "Today is for studies" for any time.

day = int(input('enter the day number : '))
session = int(input('enter the session number : '))

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
