def spy_game():
    listop = list(map(int, input().split()))
    code = [0, 0, 7]
    index = 0

    for i in listop:
        if i == code[index]:  
            index += 1  
        if index == len(code):
            return True

    return False 