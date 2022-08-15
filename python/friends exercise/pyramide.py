height = int(input('enter height of pyramide : '))

for i in range(height):
    indent = i
    width = height - i
    print(" "*indent + "* "*width)

