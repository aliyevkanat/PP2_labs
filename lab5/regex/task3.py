import re
text = input()
pattern = re.findall("[a-z]_+[a-z]+", text)
print(*pattern)
