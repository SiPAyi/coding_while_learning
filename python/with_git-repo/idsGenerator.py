from idGenerator import random_user_idGen

lengthOfId = int(input('what is the length of your id : '))
numberOfIds = int(input('how many ids do you want : '))

for i in range(numberOfIds):
    id = random_user_idGen(lengthOfId)
    print(id)

    