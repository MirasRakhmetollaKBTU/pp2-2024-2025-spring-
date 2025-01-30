def gram_to_ounce(gram : float):
    ounce = gram * 28.3495231
    return ounce

gram = float(input("Enter your number: "))
print (f"gram : {gram} => ounce : {gram_to_ounce(gram)}") 