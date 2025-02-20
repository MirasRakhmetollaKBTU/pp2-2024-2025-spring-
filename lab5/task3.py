import re

txt    = input("Enter : ")
result = re.findall(r"\b[a-z]+(?:_[a-z]+)+\b", txt)
print(result)