import string

def generate_text_files():
    alphabet = string.ascii_uppercase
    
    for letter in alphabet:
        filename = f"{letter}.txt"
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}\n")
        print(f"File '{filename}' has been created.")

if __name__ == "__main__":
    generate_text_files()
