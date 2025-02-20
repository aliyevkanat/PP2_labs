import math
sides_number = float(input("Input number of sides: "))
sides_length = float(input("Input the length of a side: "))
apofema = sides_length / (2 * math.tan(math.pi / sides_number))
area = int(0.5 * apofema * sides_number * sides_length)
print(area)