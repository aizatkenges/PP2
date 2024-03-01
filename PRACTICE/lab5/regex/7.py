def snake_to_camel(snake_case_str):
    
    words = snake_case_str.split('_')
    
  
    camel_case_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    
    
    camel_case_str = ''.join(camel_case_words)
    
    return camel_case_str

if __name__ == "__main__":
    snake_case_str = input("Enter a snake case string: ")
    camel_case_str = snake_to_camel(snake_case_str)
    print("Camel case string:", camel_case_str)
