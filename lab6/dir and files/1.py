import os

def list_directories_and_files(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

    print("\nAll Directories and Files:")
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            print(os.path.join(root, directory))
        for file in files:
            print(os.path.join(root, file))

# Example usage:
specified_path = input("Enter the path: ")
list_directories_and_files(specified_path)
