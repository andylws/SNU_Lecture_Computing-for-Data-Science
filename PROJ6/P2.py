def P2(x, y):
    # x, y: int

    def DtoB(num):
        binary = ''
        while num > 0:
            if num % 2 == 0:
                binary = '0' + binary
                num = num // 2
            else:
                binary = '1' + binary
                num = num // 2
        return binary

    x_bi = DtoB(x)
    y_bi = DtoB(y)

    while len(x_bi) != len(y_bi):
        if len(x_bi) > len(y_bi):
            y_bi = '0' + y_bi
        elif len(x_bi) < len(y_bi):
            x_bi = '0' + x_bi
        else:
            return 'ERROR'

    count = 0

    for i in range(len(x_bi)):
        if x_bi[i] != y_bi[i]:
            count = count + 1

    return count

    # return type: int
