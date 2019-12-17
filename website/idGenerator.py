from random import randint

def idGenerator(length):
    characters = "1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+=-}{?.>,<QWERTYUIOPLKJHGFDSAZXCVBNM"
    userID = ""
    for i in range(len(characters)):
        num = randint(0, len(characters)-1)
        userID += characters[num]
    return userID

