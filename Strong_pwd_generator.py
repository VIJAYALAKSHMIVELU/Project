import random
import string
def generator_pswd(length):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation
    all_chars = upper + lower + digits + special
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
        ]
    password += random.choices(all_chars, k = length-4)
    random.shuffle(password)
    return ''.join(password)
while True:
    try:
        user_length = int(input('Enter the desired password length(min 8):'))
        if user_length <8:
            print("password length must be at least 8, Pls try again.")
        else:
            break
    except ValueError:
        print("Invalid input")
strong_password = generator_pswd(user_length)
print("generated password:", strong_password)