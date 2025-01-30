def spy_game(nums : list):
    a_cash = False
    b_cash = False
    c_cash = False
    index = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            a_cash = True
            index = i
            break
    
    for i in range(index, len(nums)):
        if nums[i] == 0:
            b_cash = True
            index = i
            break
    
    for i in range(index, len(nums)):
        if nums[i] == 7:
            c_cash = True
            index = i
            break

    if a_cash and b_cash and c_cash:
        print(True)
    else:
        print(False)

spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 