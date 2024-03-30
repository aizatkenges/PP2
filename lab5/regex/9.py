import re

def insert_spaces(string):
    
    modified_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', string)
    return modified_string

if __name__ == "__main__":
    string = input("Enter a string: ")
    modified_string = insert_spaces(string)
    print("Modified string with spaces between words starting with capital letters:")
    print(modified_string)
