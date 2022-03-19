import string
import random


characters = list(string.ascii_letters + string.digits + "!@#$%&*")


def password_generator():
    length = 10
    # shuffling the characters
    random.shuffle(characters)
    # picking random characters from the list
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    # shuffling the resultant password
    random.shuffle(password)

    # converting the list to string
    return "".join(password)
