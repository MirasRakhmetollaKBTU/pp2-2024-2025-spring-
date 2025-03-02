def squares(begin, end):
    for i in range(begin, end + 1):
        yield i * i

n = int(input("Enter First number -> "))
s = int(input("Enter First number -> "))

R = squares(n, s)
for i in R:
    print(i)
