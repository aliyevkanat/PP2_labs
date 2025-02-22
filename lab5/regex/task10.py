import re

def to_snake(txt):
    return txt.group(1) + "_" + txt.group(2)

text = input()
pattern = re.sub("([^A-Z]+?)([A-Z])", to_snake, text).lower()
print(pattern)