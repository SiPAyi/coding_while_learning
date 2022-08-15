# Ask the user to enter T or S or R. If the entered string is T then print formula of
# the area of the triangle. If the entered string is S then print formula of the area of
# the square. If it is R then print formula of the area of the rectangle.


uInput = input('enter T or S or R : ')

t = "0.5 * base * height"
s = "side * side"
r = "length * breadth"

if uInput.lower() == 't':
    print(t)
elif uInput.lower() == 'r':
    print(r)
elif uInput.lower() == 's':
    print(s)
else:
    print('no formula available!!')