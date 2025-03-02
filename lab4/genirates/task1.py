def square(number):
    for i in range(1, number + 1):
        yield i * i

N = int(input("Enter your number -> "))
square_number = square(N)

for i in square_number:
    print(i)
