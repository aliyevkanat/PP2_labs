import re
text = input()
pattern = re.split("[A-Z]", text)
print(*pattern)