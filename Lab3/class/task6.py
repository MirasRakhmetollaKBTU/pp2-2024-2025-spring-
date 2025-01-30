def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

numbers       = list(range(1, 100))
prime_numbers = list(filter(lambda x : is_prime(x), numbers))
print(prime_numbers)
