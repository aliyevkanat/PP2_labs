#Write a Python program to insert spaces between words starting with capital letters.

import re

text = input()

def f(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(f(text))