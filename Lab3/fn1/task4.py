def make_prime(number : int):
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

my_list = []
a = int(input("Enter quantity of elements: "))

for i in range(a):
    cash = int(input("Enter a number : "))
    if make_prime(cash):
        my_list.append(cash)
    del cash

print(my_list)