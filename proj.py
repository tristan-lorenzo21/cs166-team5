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
        # import requests

        # url = "https://wordsapiv1.p.rapidapi.com/words/"

        # querystring = {"random":"true"}

        # headers = {
	    #     "X-RapidAPI-Key": "428f72a9f9msh71aa9e090b81f69p1b4d14jsnb8a4fa7e93d4",
	    #     "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
        # }   

        # data = requests.get(url, headers=headers, params=querystring).json()
        print("Random word: ", data)
    elif response == 2:
        print("\nGenerating a password")
    elif response == 3:
        password_input = input("Input the password you want to test: \n")
        print("Password strength of " , password_input, "is strong")
    else:
        print("\nExiting program")
        break
