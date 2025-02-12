import math

height      = int(input("Enter height: "))
first_base  = int(input("Enter width:  "))
second_base = int(input("Enter height: "))

midle = (first_base + second_base) / 2
area  = midle * height

del height
del first_base
del second_base
del midle

print(f"Area of trapezoid is {area}")

del area