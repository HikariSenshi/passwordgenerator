import random
import string

CHARS = string.ascii_letters + string.digits + "~!@#$%^&()_+="


def pwd_generator(strings_count=1):

    for i in range(0, strings_count):

        string_length = random.randint(1, 10)
        yield str(''.join(random.choice(CHARS) for i in range(string_length)))
