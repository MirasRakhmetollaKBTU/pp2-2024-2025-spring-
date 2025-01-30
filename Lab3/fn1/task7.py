def has_33(nums : list):
    b_cash = False
    for i in range(1, len(nums)):
        if nums[i - 1] == nums[i] == 3:
            b_cash = True

    print(b_cash)

has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])