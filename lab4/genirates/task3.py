def three_and_four(number):
    for i in range(number):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter your number -> "))
R = three_and_four(n)
print(", ".join(map(str, R)))
