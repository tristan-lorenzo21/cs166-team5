import requests
import json
import random
import string
import secrets

from random_word import Wordnik
from secret import api_key
from password_evaluate import password_evaluate

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
        # generates a random number that will be used to generate the amount of words the api request will produce
        word_num = random.randint(5, 6)

        # api request that gets the random words
        response = requests.get("https://api.wordnik.com/v4/words.json/randomWords?hasDictionaryDef=true&minCorpusCount=10000&maxCorpusCount=-1&minDictionaryCount=10&maxDictionaryCount=-1&minLength=5&maxLength=8&limit={}&api_key={}".format(word_num, api_key))
        
        # array where the words will be stored
        word_array = []

        # pulls the words from each object that was returned from the api request
        for obj in response.json():
            word_array.append((obj['word']))

        # pulls a random word from word_array that will be capitalized
        arr_len = len(word_array) - 1
        random_index = random.randint(1, arr_len)

        # holds the words that will be returned
        ret_array = []

        # generates a random number that will be appended to the returned array
        random_number = random.randint(0,9)

        # generates a random special character that will be appened to the returned array
        special_characters = string.punctuation
        random_special_char = secrets.choice(special_characters)

        # capitalizes the random word that was picked
        for index, word in enumerate(word_array):
            if index == random_index:
                ret_array.append(word.capitalize())
            else:
                ret_array.append(word)

        # adds the random number and special character to the returned passphrase
        ret_array.append(str(random_number))
        ret_array.insert(0, random_special_char)

        # returns the generated passphrase
        print("Generated Passphrase: " + ' '.join(ret_array))   
    elif response == 2:
        # define the alphabet
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation

        alphabet = letters + digits + special_chars

        # fix password length
        pwd_length = 16

        # generate a password string
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        # generate password meeting constraints
        while True:
            pwd = ''
            for i in range(pwd_length):
                pwd += ''.join(secrets.choice(alphabet))

            if (any(char in special_chars for char in pwd) and 
                sum(char in digits for char in pwd)>=2):
                break
        print("password: " + pwd)
    elif response == 3:
        password_input = input("Input the password you want to test: \n")
        password_evaluate(password_input)
    else:
        print("\nExiting program")
        break
