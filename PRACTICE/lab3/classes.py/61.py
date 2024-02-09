
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == "__main__":
  
    numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 40, 41, 43, 47, 50]

    
    prime_numbers = list(filter(lambda x: is_prime(x), numbers))

    print("Prime numbers in the list:", prime_numbers)
