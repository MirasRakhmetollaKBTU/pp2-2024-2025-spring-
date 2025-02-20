import re

txt    = input("Enter : ")
result = re.sub(r"(?<!^)(?=[A-Z])", lambda x : " " + x.group(0), txt)
print(result)
