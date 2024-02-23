def countdown(n):
    while n >= 0:
        yield n
        n -= 1


n = 5
countdown_generator = countdown(n)

for num in countdown_generator:
    print(num)
