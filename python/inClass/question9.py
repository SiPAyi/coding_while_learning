# enerally we say leap year, if the year is divisible by 4 for normal years like 1976, 1788,
# 2012 etc. If the years are like centuries 300,400,1300,1500,600,1800 etc then it should be
# divisible by 400 then only we call the year as leap year


year = int(input('enter year : '))

# if year % 4 == 0:
#     if year % 100 == 0 and year % 400 != 0:
#         print('not leap year !!')
#     else:
#         print('leap year ')
# else:
#     print('not leap year')


if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('leap year')
else:
    print('not leap year!')