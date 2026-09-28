import random
import string


def make_password(length=8):
    """Return a random password of letters and digits."""
    characters = string.ascii_letters + string.digits
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password


print(make_password())     # e.g. hhKale6l
print(make_password(12))   # e.g. 4Tq9bLmZx2Pa