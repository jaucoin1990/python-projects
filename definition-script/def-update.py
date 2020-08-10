import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

def similar(word1, dict=data):
    list = dict.keys()
    return get_close_matches(word1, list, cutoff=.75)


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
               break
    else:
        print("I don't know that word. Try a different word.")
