def insert(l : list):
    for element_l in range(len(l)):
        print('*' * l[element_l])

lis = []
a   = int(input("Enter quantity of elements : "))
for i in range(a):
    cash = int(input("Enter numbers: "))
    lis.append(cash)
    del cash

insert(lis)
