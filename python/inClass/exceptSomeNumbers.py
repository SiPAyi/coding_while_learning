# print 1 to 100 number and skip the numbers from 20 to 50

for i in range(1,101):
    if i < 20 or i > 50:
        print(i,end=' ')

for i in range(1,100):
    if 19 < i < 50:
        continue
    print(i)
