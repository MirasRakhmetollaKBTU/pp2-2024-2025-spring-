import math

Sides  = int(input("Enter number of side: "))
Length = int(input("Enter length of side: "))

P = Sides * Length **2
S = P / (4 * math.tan(math.pi / Sides))

del P
del Sides
del Length

print (f"The area if the polygon is {S:.0f}")

del S