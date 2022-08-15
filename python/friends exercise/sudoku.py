## to create one box
# from random import randint

# values = [1, 2, 3, 4, 5, 6, 7 ,8, 9]
# box = []

# for i in range(9):
#     cell = values[randint(0, len(values)-1)]
#     values.remove(cell)
#     box.append(cell)
#     # print(i+1)


# for i in range(9):
#     print(box[i], end='')
#     if (i+1)%3 == 0:
#         print()
#     else:
#         print(' | ', end='')




## to create 9 boxes
from random import randint

values = [1, 2, 3, 4, 5, 6, 7 ,8, 9]
sudoku = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
]

sudoku = []
for i in range(1):
    row = []
    for i in range(3):
        row.append(i)

for box in sudoku:
    for i in range(9):
        print(box[i], end='')
        if (i+1)%3 == 0:
            print()
        else:
            print(' | ', end='')
    print()