def P1(num_list):
    ans = 0
    for i in range(len(num_list)):
        for j in range(len(num_list)-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                ans += 1
    return ans


def P2(lst):
    lst.sort()
    lst.sort(key=len)
    return lst


def P3(matrix):
    # 대각 성분 끼리는 i-j가 같은 것을 이용
    dct = dict()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i-j in dct:
                dct[i-j].append(matrix[i][j])
            else:
                dct[i-j] = [matrix[i][j]]
    for key in dct:
        dct[key].sort()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = dct[i-j].pop(0)
    return matrix


def P4(A, B):
    A.sort()
    B.sort(reverse=True)
    ans = 0
    for i in range(len(A)):
        ans += A[i] * B[i]
    return ans


def P5(lst):
    n = len(lst)
    conti = [0] * (n+1)
    # conti[num]: num까지 연속적으로 증가하는 수의 개수
    # ex) conti[10] = 4 라는 것은 lst에서 7, 8, 9, 10 이 순서를 이루고 있음
    # (각 수 사이에는 다른 수가 있을 수도 있고, 6은 7 이후에 위치함)
    for num in lst:
        conti[num] = conti[num-1] + 1
    # 최대 개수로, 연속적으로 정렬된 순서인 수를 제외한 나머지에 수에 대해
    # 적절한 순서로 적절한 행동을 취하면 정렬된 수를 만들 수 있음
    # 이것 보다 적은 행동으로 정렬할 수 없다는 것은 증명 가능
    return n - max(conti)
