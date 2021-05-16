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


def P6_ans(num_list: List[float]) -> List[float]:
    # You don't actually need this part. This is for grading purpose
    out_list = copy.deepcopy(num_list)

    out_list.remove(3382)  # Remove 3382
    out_list.extend([5566, 1830])  # Add 5566, 1830
    # Sort ascending, you can also use sorted(), but note that syntax is different
    out_list.sort()

    return out_list


def P7_ans(nested_list: list) -> list:
    out_list = []
    out_list.append(nested_list[0][0])  # Add the first element of first list
    # Add the last element of the second list
    out_list.append(nested_list[1][-1])
    return out_list
    # nested_list[0][0], nested_list[1][-1] is wrong, it is a Tuple, not a list


def P8_ans(rat_1: list, rat_2: list, measure_day: int) -> bool:
    return rat_1[measure_day - 1] > rat_2[measure_day - 1]


def P9_ans(rat_1: list, rat_2: list) -> list:
    L1 = []
    # Append each element of two lists alternately
    for i in range(len(rat_1)):
        L1.append(rat_1[i])
        L1.append(rat_2[i])
    return L1


def P10_ans(start_i: int, end_i: int) -> list:
    # Make a list in the range between start_i and end_i
    return list(range(start_i, end_i + 1))
