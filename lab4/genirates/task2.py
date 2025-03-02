def even(number):
    for i in range(2, number, 2):
        yield i

n = int(input("Enter your number -> "))
R = even(n)
print(", ".join(map(str, R)))
