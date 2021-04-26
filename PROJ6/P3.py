def P3(num):
    # num: int

    def DtoB(de):
        binary = ''
        while de > 0:
            if de % 2 == 0:
                binary = '0' + binary
                de = de // 2
            else:
                binary = '1' + binary
                de = de // 2
        return binary

    def BtoD(bi):
        de = 0
        for i in range(len(bi)):
            de = de + int(bi[-(i + 1)]) * 2 ** i
        return de

    num_bi = DtoB(num)

    while len(num_bi) < 32:
        num_bi = '0' + num_bi

    num_bi_reverse = num_bi[::-1]

    result = BtoD(num_bi_reverse)

    return result

    # return type: int
