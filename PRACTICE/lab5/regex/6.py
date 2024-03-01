def replace_chars_with_colon(text):
    
    replaced_text = text.replace(' ', ':').replace(',', ':').replace('.', ':')
    return replaced_text

if __name__ == "__main__":
    text = input("Enter a string: ")
    replaced_text = replace_chars_with_colon(text)
    print("Original string:", text)
    print("String after replacement:", replaced_text)
