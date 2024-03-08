def write_list_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"List has been successfully written to '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    data = ["apple", "banana", "orange", "grape", "pineapple"]
    filename = input("Enter the filename to write the list: ")
    write_list_to_file(filename, data)
