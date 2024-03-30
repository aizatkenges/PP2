def divisible_by_3_and_4(n):
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

# Example usage:
n = 20
generator = divisible_by_3_and_4(n)

for number in generator:
    print(number)
