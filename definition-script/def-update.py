import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))
data = {k.lower(): v for k, v in data.items()}


def similar(word1, dict=data):
    list = dict.keys()
    return get_close_matches(word1, list, cutoff=.75)


def value_returner(key, file=data):
    return file[key]


print("This is a dictionary. Enter the word you'd like defined. When you're done using me to define words, type 'end' instead of a word.")

while True:
    key = input("\nEnter word: ").lower()

    if key == "end":
        break
    elif key in data:
        list = value_returner(key)
        print("\nYour definition is:\n")
        for i in list:
            print("\n{}\n".format(i))
    elif similar(key):
       list = similar(key)
       for i in list:
           print("\nDid you mean {}?".format(i))
           answer = input("\nYes or no? ").lower()
           if answer == "yes" or answer == "y":
               new_list = value_returner(i)
               print("\nYour definition is:\n")
               for i in new_list:
                   print("\n{}\n".format(i))
               break
    else:
        print("I don't know that word. Try a different word.")
        
