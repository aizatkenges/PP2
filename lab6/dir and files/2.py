import os

def check_path_access(path):
    # Check if the path exists
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return

    # Check readability
    if os.access(path, os.R_OK):
        print(f"Read access to '{path}' is allowed.")
    else:
        print(f"Read access to '{path}' is not allowed.")

    # Check writability
    if os.access(path, os.W_OK):
        print(f"Write access to '{path}' is allowed.")
    else:
        print(f"Write access to '{path}' is not allowed.")

    # Check executability
    if os.access(path, os.X_OK):
        print(f"Execute access to '{path}' is allowed.")
    else:
        print(f"Execute access to '{path}' is not allowed.")

if __name__ == "__main__":
    specified_path = input("Enter the path to check: ")
    check_path_access(specified_path)
