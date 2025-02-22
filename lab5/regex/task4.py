import re
text = input()
pattern = re.findall("[A-Z]{1}[a-z]+", text)
print(*pattern)