import requests
import json
from random_word import Wordnik
wordnik_service = Wordnik()

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

    response = int(input())

    if response == 1:
        print("Random word: ")
    elif response == 2:
        print("\nGenerating a password")
    elif response == 3:
        password_input = input("Input the password you want to test: \n")
        print("Password strength of " , password_input, "is strong")
    else:
        print("\nExiting program")
        break
