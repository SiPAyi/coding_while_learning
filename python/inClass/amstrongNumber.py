# number = 153
# sumOfDigits = 1**3 + 5**3 + 3**3
# number == sumOfDigits

number = input('enter the number : ')

sum = 0
for i in number:
    sum = sum + int(i) ** len(number)


if sum == int(number):
    print('its a strong number bro!!')
else:
    print('its not a strong number bro!!')
