import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Passwork with", length, "characters:", result_str)

get_random_string(8)
get_random_string(6)
get_random_string(4)
