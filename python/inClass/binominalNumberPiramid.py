height = 10

for row in range(1,height):
    print('  '*(height-row) ,end='')
    
    for k in range(1, row+1):
        print(k, end=' ')
    for h in range(row-1, 0 , -1):
        print(h, end=' ')
    print()

for row in range(1,height):
    print('  '*row, end='')
