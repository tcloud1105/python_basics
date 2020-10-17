import json
from difflib import get_close_matches

data = json.load(open('data1.json'))

def translate(w):
    w = w.lower()
    if w in data:
         return data[w]
    else:
        return "the word doesn't exist. Please double check it."

word = input("Enter a word: ")
print(translate(word))