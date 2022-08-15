from random import randint
import string

def random_user_idGen(lengthOfrandom_user_id):
    abcd = string.ascii_letters
    random_user_id = ""

    for i in range(lengthOfrandom_user_id):
        value = randint(0,34)
        if value < 26:
            random_user_id += abcd[value]
        else:
            number = int(value)-25
            random_user_id += str(number)
    return random_user_id

print(random_user_idGen(randint(0,6)))
    
