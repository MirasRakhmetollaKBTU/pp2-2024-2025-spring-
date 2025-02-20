import re

txt    = input("Enter : ")
result = re.search(r"ab{2,3}", txt)
print(result)