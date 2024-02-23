def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

# Test the generator with a for loop
a = 3
b = 7

for square in squares(a, b):
    print(square)
