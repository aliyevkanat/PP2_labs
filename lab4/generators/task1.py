def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2 
        
n = int(input())
for i in square_generator(n):
    print(i)