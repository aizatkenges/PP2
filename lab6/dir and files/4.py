def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
        return -1

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    lines = count_lines(filename)
    if lines != -1:
        print(f"The number of lines in the file '{filename}' is: {lines}")
