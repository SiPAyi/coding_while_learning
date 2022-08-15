alpha = []

for i in range(5):
    a = input('enter the element : ')
    alpha.append(a)

for i in range(len(alpha)):
    alpha.insert(i, alpha[-1])
    del(alpha[-1])

print(alpha)