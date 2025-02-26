orig = open('for-task7[o].txt', 'r')
copy = open('for-task7[i].txt', 'w')

how_m = int(input("how many content : "))
list  = []

for i in range(how_m):
    cash = int(input(f"Enter line for copy {i + 1} : ")) - 1
    list.append(cash)
    del cash

all_lines = orig.readlines()

for i in list:
    content = orig.readline(list[i])
    copy.write(all_lines[i])
    del content


orig.close()
copy.close()

copy = open('for-task7[i].txt', 'r')
print(copy.read())
