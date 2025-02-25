work = input("Enter sentence : ")
upper_letter = 0
lower_letter = 0

for i in work:
    if i.islower():
        lower_letter += 1
    elif i.isupper():    
        upper_letter += 1

print (f"quantity of:\nLower case is {lower_letter}\nUpper case is {upper_letter}")
