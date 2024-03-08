import time
import math

def calculate_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)  # Convert milliseconds to seconds
    result = math.sqrt(number)
    return result

if __name__ == "__main__":
    number = int(input("Enter the number: "))
    milliseconds = int(input("Enter the number of milliseconds: "))

    square_root = calculate_square_root(number, milliseconds)
    print(f"Square root of {number} after {milliseconds} milliseconds is {square_root}")
