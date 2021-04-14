def P3(A, B):
    '''
    A, B: list
    '''
    length = len(A)

    for i in range(length):
        sub_sum_A = 0
        sub_sum_B = 0
        sub_list_A = []
        sub_list_B = []
        for j in range(i + 1):
            sub_list_A = A[j: length - i + j]
            sub_list_B = B[j: length - i + j]
            sub_sum_A = sum(sub_list_A)
            sub_sum_B = sum(sub_list_B)
            if sub_sum_A == sub_sum_B:
                return len(sub_list_A)
            else:
                continue

    return 0

    # return type: integer
