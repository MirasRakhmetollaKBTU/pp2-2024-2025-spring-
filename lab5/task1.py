import re

with open("row.txt", "r", encoding="UTF=8") as file:
    txt = file.read()

dates = re.findall(r"ab*", txt)
print(dates)
