import re

def split_at_uppercase(string):
    
    split_strings = re.findall('[A-Z][^A-Z]*', string)
    return split_strings

if __name__ == "__main__":
    string = input("Enter a string: ")
    split_strings = split_at_uppercase(string)
    print("Strings after splitting at uppercase letters:")
    for split_str in split_strings:
        print(split_str)
