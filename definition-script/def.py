import json
from difflib import SequenceMatcher

data = json.load(open("data.json", "r"))

def similar(word1, dict=data):
    word_suggestions = []
    for key in dict:
        ratio = SequenceMatcher(None, word1, key).ratio()
        if ratio > .8:
            word_suggestions.append(key)
    return word_suggestions



def value_returner(key, file=data):
    return file[key]

print("This is a dictionary. Enter the word you'd like defined. When you're done, type 'end.'")
while True:
    key = input("Enter word: ").lower()

    if key == "end":
        break
    elif key in data:
        print(value_returner(key))
    elif similar(key):
       list = similar(key)
       for i in list:
           print("Did you mean {}?".format(i))
           answer = input("Yes or no? ").lower()
           if answer == "yes":
               print(value_returner(i))
    else:
        print("I don't know that word. Try a different word.")



