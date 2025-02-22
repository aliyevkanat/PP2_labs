import re
text = input()
pattern = re.findall("a.*b$", text)
print(*pattern)