import re

def match_pattern(text):
    pattern = r'^a(b*)$'  
    if re.match(pattern, text):
        print(f"String '{text}' matches the pattern.")
    else:
        print(f"String '{text}' does not match the pattern.")

if __name__ == "__main__":
    text = input("Enter a string: ")
    match_pattern(text)
