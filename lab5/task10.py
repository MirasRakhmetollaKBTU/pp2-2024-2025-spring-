import re

txt    = input("Enter : ")
result = re.sub(r"[A-Z]", lambda x : "_" + x.group(0).lower(), txt)
print(result)