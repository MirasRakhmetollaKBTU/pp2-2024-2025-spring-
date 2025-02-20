import re

txt    = input("Enter : ")
result = re.split(r"(?<!^)(?=[A-Z])",txt)
print(result)