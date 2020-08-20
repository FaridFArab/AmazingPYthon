import random
import string


def get_random_password(length):
    password = ''
    password_character = string.ascii_letters + string.digits + string.punctuation
    for i in range(length):
        password = password + password.join(random.choice(password_character))
    print('Your Password:' + password)


get_random_password(15)
