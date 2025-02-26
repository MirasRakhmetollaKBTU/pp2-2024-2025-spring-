import os

dir_name = "Task6"

if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Directory {dir_name} is created.")
else:
    print(f"Directory {dir_name} already exists.")



letter = 'A';
for i in range(26):
    cash = open(f"Task6/{chr(ord(letter) + i)}.txt", 'x')
    cash.close()
