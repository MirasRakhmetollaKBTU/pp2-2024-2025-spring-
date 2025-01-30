def filt(l : list):
    nl = []
    for i in l:
        if i not in nl:
            nl.append(i)

    return nl

ml = []
a  = int (input("Enter how much elements: "))

for i in range(a):
    cash = int(input("element: "))
    ml.append(cash)
    del cash

print(filt(ml))
