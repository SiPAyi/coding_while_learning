diagnal = int(input('enter the diagnal length : '))

for i in range(1, diagnal+1):
    print(" "*(diagnal-i)," *"*i)

for i in range(1,diagnal+1):
    print(" "*i, ' *'*(diagnal-i))