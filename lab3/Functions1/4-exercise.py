def filter_prime():
    numbers = list(map(int, input().split()))
    for i in numbers:
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            print(i)