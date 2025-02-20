import re

txt    = input("Enter : ")
result = re.sub("[ ,.]", ":", txt)
print(result)
