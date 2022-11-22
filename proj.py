import requests
import json
import random

from random_word import Wordnik
from secret import api_key

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

    response = int(input("\n"))

    if response == 1:
        # 
        word_num = random.randint(5, 6)
        response = requests.get("https://api.wordnik.com/v4/words.json/randomWords?hasDictionaryDef=true&minCorpusCount=10000&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength=8&limit={}&api_key={}".format(word_num, api_key))
        word_array = []

        for obj in response.json():
            word_array.append((obj['word']))

        print("Generated Passphrase: " + ' '.join(word_array))   
    elif response == 2:
        print("\nGenerating a password")
    elif response == 3:
        password_input = input("Input the password you want to test: \n")
        print("Password strength of " , password_input, "is strong")
    else:
        print("\nExiting program")
        break
