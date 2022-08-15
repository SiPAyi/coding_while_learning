side = int(input('enter the size of square : '))

for i in range(side):
    if i == 0 or i == (side-1):
        print("* "*side)
    else:
        print("* "+"  "*(side-2)+"* ")