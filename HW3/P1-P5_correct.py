def P1_ans(L: list) -> bool:
    return L[0] == L[-1]
    # "is" could be different than "==", but not included in grading case


def P2_ans(L1: list, L2: list) -> bool:
    return len(L1) > len(L2)


def P3_ans(L1: list) -> list:
    return [i+1 for i in L1]


def P4_ans(start_i: int, end_i: int) -> float:
    sum_i = 0
    cnt = 0

    # Loop through all integers in the range
    for i in range(start_i, end_i+1):
        sum_i += i
        cnt += 1

    # Calculate average and return
    return sum_i / cnt


def P5_ans(num_list: List[float]):
    index = 0

    # Use while loop and when negative numbers are met, do not increase the index
    while index < len(num_list):
        if num_list[index] < 0:
            del num_list[index]
        else:
            index += 1

    return num_list

    # This is also graded as correct answer
    new_list = []
    for item in num_list:
        if item >= 0:
            new_list.append(item)

    return new_list
