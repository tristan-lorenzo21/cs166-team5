import requests
import json
import random
import string
import secrets

from secret import api_key

def generate_passphrase(): 
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