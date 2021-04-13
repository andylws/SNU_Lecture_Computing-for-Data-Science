def P1(nums, k):
    '''
    nums: list, k: int
    '''
    r_dict = {}
    result = None

    for i in range(k):
        r_dict[i] = 0

    print(r_dict)

    for num in nums:
        remainder = num % k
        r_dict[remainder] = r_dict[remainder] + 1

    print(r_dict)

    if r_dict[0] % 2 == 0:
        result = True
        for i in range(1, k // 2 + 1):
            if r_dict[i] != r_dict[k - i]:
                result = False
                return result
            else:
                result = True
    else:
        result = False

    return result

    # return type: bool
