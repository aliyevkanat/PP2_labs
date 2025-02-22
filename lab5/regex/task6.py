import re

text = input()
pattern = re.sub("[ ,.]", ":", text)
print(pattern)