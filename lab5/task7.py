import re

txt    = input("Enter : ")
result = re.sub("_([a-z])", lambda x : x.group(1).upper(), txt)
print(result)