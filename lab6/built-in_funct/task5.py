t_input  = input("Enter issue (a,b,c,...) : ")
my_tuple = eval(f"({t_input})")
print(f"The touple {my_tuple} is : {all(my_tuple)}")
