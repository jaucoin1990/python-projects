import string
english_alphabet = list(string.ascii_uppercase)


def upper_checker(string):
    string_list = []
    
    if type(string) == str:
        string_list = list(string)

        if string_list[0] in english_alphabet:
            return "'{}' starts with an upper-case letter between A-Z.".format(string)
            #can also print statement here
        else:
            return "This string does not start with an upper-case letter better A-Z."
    else:
        return "This string does not start with an upper-case letter better A-Z."
print(upper_checker("this is a string"))
print(upper_checker("This is another string"))
print(upper_checker(1234455))
print(upper_checker("字母"))
