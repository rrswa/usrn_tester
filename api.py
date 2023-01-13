import requests
import random


def test_usrn(before_query, after_query, letter_amount):
    output_file = open('outputs/output.txt', 'a')

    letters = ["a", "b", "c", "d", "e",
               "f", "g", "h", "i", "j",
               "k", "l", "m", "n", "o",
               "p", "q", "r", "s", "t",
               "u", "v", "w", "x", "y",
               "z"
               ]

    wordArray = []

    while True:
        ha_id = ''

        i = 0
        while i < 5:
            ha_id += letters[random.randint(0, 25)]
            i += 1

        if ha_id in wordArray:
            break

        wordArray.append(ha_id)

        req = requests.get(f"{before_query}{ha_id}{after_query}")

        if req.status_code == 200:
            print(ha_id)
