import string
import secrets

def generate_password():
    # define the alphabet
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    chars = letters + digits + special_chars

    # fix password length
    pwd_length = 16

    # generate a password string
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(chars))

    # generate password meeting constraints
    while True:
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(chars))

        if (any(char in special_chars for char in pwd) and 
            sum(char in digits for char in pwd)>=1):
            break

    print("password: " + pwd)