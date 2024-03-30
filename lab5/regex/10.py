import re

def camel_to_snake(camel_case_str):
    snake_case_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_str).lower()
    return snake_case_str

if __name__ == "__main__":
    camel_case_str = input("Enter a camel case string: ")
    snake_case_str = camel_to_snake(camel_case_str)
    print("Snake case string:", snake_case_str)
