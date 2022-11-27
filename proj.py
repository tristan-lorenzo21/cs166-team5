from password_evaluate import password_evaluate
from passphrase_generator import generate_passphrase
from password_generator import generate_password


def print_menu():
    print("""
    --------------------------------------------
    | Enter the number of the desired function |
    |                                          |
    | 1. Generate a passphrase                 |
    | 2. Generate a password                   |
    | 3. Test password strength                |
    | 4. Exit program                          |
    --------------------------------------------
    """)

while True:
    print_menu()

    response = int(input("\n"))

    if response == 1:
        generate_passphrase()
    elif response == 2:
        generate_password()
    elif response == 3:
        password_input = input("Input the password you want to test: \n")
        password_evaluate(password_input)
    else:
        print("\nExiting program")
        break
