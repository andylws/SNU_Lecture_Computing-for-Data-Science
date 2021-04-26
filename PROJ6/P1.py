def P1(num):
    # num: int
    count = 0
    n = num
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            count = count + 1
            n = n // 2

    return count

    # return type: int
