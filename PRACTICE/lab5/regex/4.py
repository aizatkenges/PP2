import re

def find_sequences(text):
    pattern = r'[A-Z][a-z]+'  
    sequences = re.findall(pattern, text)
    return sequences

if __name__ == "__main__":
    text = input("Enter a string: ")
    result = find_sequences(text)
    if result:
        print("Sequences of one uppercase letter followed by lowercase letters:")
        for seq in result:
            print(seq)
    else:
        print("No sequences found.")
