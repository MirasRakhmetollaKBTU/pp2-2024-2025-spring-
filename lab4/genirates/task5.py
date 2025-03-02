def to_zero(n):
    for i in range (n, -1, -1):
        yield i

n = int(input("Enter number: "))
g = to_zero(n)

for i in g:
    print(i)
