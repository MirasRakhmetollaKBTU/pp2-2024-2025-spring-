import math

number   = input("Enter number (a,b,...) : ")
num_list = [int(x.strip()) for x in number.split(",")]
product  = math.prod(num_list)
print(f"the product of number is {product}")
