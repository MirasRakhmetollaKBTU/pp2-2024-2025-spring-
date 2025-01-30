import math   

def volume(radius : int):
    return (4 * pow(radius, 3) * math.pi) / 3

rad = int(input("Enter radious of sphere: "))
print(f"Volum of sphere: {volume(rad)}")