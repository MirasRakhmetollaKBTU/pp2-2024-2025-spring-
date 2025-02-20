import re

txt    = input("Enter : ")
result = re.search(r"\ba.*b$\b", txt)
print(result)