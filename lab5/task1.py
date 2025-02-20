import re 

txt    = input("Enter : ")
result = re.search(r"ab*", txt)
print(result)