def divisible(n):
    for i in range(1, n + 1):
        if i % 4 == 0 and i % 3 == 0:
         yield i
        
        
n = int(input())
for i in divisible(n):
    print(i)