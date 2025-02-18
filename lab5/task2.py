import re

with open("row.txt", "r", encoding = "UTF-8") as file:
    txt = file.read()

data = re.findall(r"ab{2, 3}", txt)
print(data)
