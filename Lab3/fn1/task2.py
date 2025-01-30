def F_to_C(F : float):
    C = (5 / 9) * (F - 32)
    return C

F = float(input("Enter Fahrenheit: "))
print (f"F : {F} => C : {F_to_C(F)}")