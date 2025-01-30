def solve(numhead : int, numlegs : int):
    chicken = numlegs // 4
    rabbit  = numhead - chicken
    return f"Rabbit : {rabbit} | chicken : {chicken}"

numhead = int(input("Enter number of head: "))
numlegs = int(input("Enter number of legs: "))

print(solve(numhead, numlegs))