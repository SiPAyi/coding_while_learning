# Write a program to check the entered year is leap year or not.
# Generally we say leap year, if the year is divisible by 4 for normal years like
# 1976, 1788, 2012 etc. If the years are like centuries 300,400,1300,1500,600,1800 etc
# Then it should be divisible by 400 then only we call the year as leap year.

year = int(input('enter the year : '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('its a leap year')
else:
    print('its not a leap year')
