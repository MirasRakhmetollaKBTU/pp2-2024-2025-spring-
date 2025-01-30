def revers_list(l : list):
    len_l = len(l) - 1
    for i in range(len_l, -1, -1):
        print(l[i] + " ")
    
    del len_l
    return

ml = []
a  = int (input("Enter quantity of elements : "))

for i in range(a):
    cash = input("Enter yout word : ")
    ml.append(cash)
    del cash

revers_list(ml)