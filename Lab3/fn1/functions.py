def gram_to_ounce(gram : float):
    ounce = gram * 28.3495231
    return ounce

def F_to_C(F : float):
    C = (5 / 9) * (F - 32)
    return C

def make_prime(number : int):
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True
