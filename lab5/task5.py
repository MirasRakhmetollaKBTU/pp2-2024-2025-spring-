import re

with open("row.txt", "r", encoding = "UTF-8") as file:
    txt = file.read()

date = re.findall("\ba.*b$\b", txt)
print(date)
