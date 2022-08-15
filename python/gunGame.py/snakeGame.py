import os, time
import random

i = 1
goal = random.randrange(15,30)

while i < goal:
    # next_step = input("yout input :  ")
    os.system('clear')
    print(' '*i+'------->',end='')
    print(' '*(goal-2-i)+ '*')
    print()
    i += 1
    time.sleep(0.1)