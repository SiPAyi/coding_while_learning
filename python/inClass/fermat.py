height = int(input('distance between object and reflecting plane : '))
base = int(input('distance between object and image : '))

leastPath = height + (height**2 + base**2)

for deltaX in range(base):
    length = (height**2 + deltaX**2)**0.5
    newKarnam = ((base - deltaX)**2 + height**2)**0.5
    pathLength = length + newKarnam

    if pathLength < leastPath:
        leastPath = pathLength
    else:
        break

print('shortest path ',leastPath,'delta x : ',deltaX-1)
