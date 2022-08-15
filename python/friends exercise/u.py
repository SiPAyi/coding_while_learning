age = int(input('enter the age'))

if age < 18:
    print('child')
elif 18 < age < 35:
    print('young')
elif 35 < age < 60:
    print('old')
else:
    print('senior citizen/retired')
