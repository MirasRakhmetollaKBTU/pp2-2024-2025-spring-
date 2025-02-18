import re

with open("row.txt", "r", encoding = "UTF-8") as file:
    txt = file.read()

data = re.findall("\b[A-Z][a-z]+\b",txt)
print(data)
