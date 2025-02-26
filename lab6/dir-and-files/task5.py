file = open('for-task5.txt', 'w')

num  = int(input("Enter size : "))
list = []

for i in range(num):
    list.append(i)

file.write(str(list))
file.close()

file = open('for-task5.txt', 'r')
print(file.read())
file.close