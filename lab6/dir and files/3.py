import os

def check_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f"The path '{path}' does not exist.")

if __name__ == "__main__":
    specified_path = input("Enter the path to check: ")
    check_path(specified_path)
