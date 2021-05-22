def P1_ans(game: list) -> int:
    cnt = 0
    rsp_dict = {'RR': 0, 'RS': 1, 'RP': -1, 'PR': 1,
                'PP': 0, 'PS': -1, 'SR': -1, 'SS': 0, 'SP': 1}
    for each_round in game:
        a = each_round[0]
        b = each_round[1]
        c = each_round[2]
        # When player 1 wins player 2
        if rsp_dict[a+b] == 1:
            # player 1 wins/draw player 3 then player 1 won.
            if rsp_dict[a+c] >= 0:
                cnt += 1
        elif rsp_dict[a+b] == 0:
            if rsp_dict[a+c] == 1:
                cnt += 1
    return cnt


def P2_ans(n: int) -> bool:
    i = 2
    m = n
    cnt = 0
    # If m can be divided by the same number more than 1 time, m cannot be factored into 2 different primes
    while m > 1 and cnt < 2:
        while m % i == 0 and cnt < 2:
            m = m / i
            cnt += 1
        i += 1
    if m == 1 and cnt == 2:
        return True
    else:
        return False
    return False


def P3_ans(info: list) -> str:
    sex = info[0]
    birth_yr = info[1]
    birth_mon = info[2]
    birth_day = info[3]
    yr_part = format(birth_yr % 100, '02')
    if birth_yr < 2000:
        sex_part = (1 if sex == 'MALE' else 2)
    else:
        sex_part = (3 if sex == 'MALE' else 4)
    return yr_part + format(birth_mon, '02') + format(birth_day, '02') + str(sex_part)
