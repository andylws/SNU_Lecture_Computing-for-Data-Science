def P2(nums):
    '''
    nums: list
    '''
    '''
    number = {0: 0, 1: 0}

    for i in range(len(nums)):
        if nums[i] == 0:
            number[0] = number[0] + 1
        elif nums[i] == 1:
            number[1] = number[1] + 1
        else:
            return "Invalid input"

    while number[0] != number[1] and number[0] * number[1] != 0:
        if number[0] > number[1]:
            if nums[0] == 0:
                del nums[0]
                number[0] = number[0] - 1
            elif nums[-1] == 0:
                del nums[-1]
                number[0] = number[0] - 1
            else:
                del nums[-1]
                number[1] = number[1] - 1
        elif number[0] < number[1]:
            if nums[0] == 1:
                del nums[0]
                number[1] = number[1] - 1
            elif nums[-1] == 1:
                del nums[-1]
                number[1] = number[1] - 1
            else:
                del nums[-1]
                number[0] = number[0] - 1

    if number[0] * number[1] == 0:
        return 0
    else:
        return number[0] + number[1]
    '''

    for i in range(len(nums)):
        sub_sum = 0
        sub_list = []
        for j in range(i + 1):
            sub_list = nums[j: len(nums) - i + j]
            sub_sum = sum(sub_list)
            if sub_sum == len(sub_list) / 2:
                return len(sub_list)
            else:
                continue

    return 0

    # return type: int
