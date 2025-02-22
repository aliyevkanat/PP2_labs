import re
text = input()
match = re.findall("ab*", text)
print(*match)