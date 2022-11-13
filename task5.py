import random
import string

def get_random_password() -> str:
    n = 8
    alphabet = string.ascii_letters + string.digits
    password = ''.join(random.sample(alphabet, n))
    return password

print(get_random_password())
