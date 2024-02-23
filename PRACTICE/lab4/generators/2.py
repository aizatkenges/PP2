def generate_even_numbers(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num

def main():
    try:
        n = int(input("Enter the value of n: "))
        if n < 0:
            print("Please enter a non-negative integer.")
            return

        even_numbers = generate_even_numbers(n)
        print("Even numbers between 0 and", n, "are:", end=" ")
        print(*even_numbers, sep=", ")

    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
