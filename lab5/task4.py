import re

txt    = input("Enter : ")
result = re.findall(r"\b[A-Z][a-z]+\b", txt)
print(result)