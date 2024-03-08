import os

def delete_file(path):
    if not os.path.exists(path):
        print(f"The file '{path}' does not exist.")
        return

    try:
        if os.access(path, os.F_OK):
            os.remove(path)
            print(f"The file '{path}' has been deleted.")
        else:
            print(f"No access to delete the file '{path}'.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {str(e)}")

if __name__ == "__main__":
    file_path = input("Enter the file path to delete: ")
    delete_file(file_path)
