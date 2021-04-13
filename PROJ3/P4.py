def P4(nums):
    '''
    nums: list
    '''
    nums_sets = set(nums)
    min_num = nums[0]
    max_num = nums[0]
    cur_num = min_num
    count = 0
    max_count = 0

    for i in nums_sets:
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i

    while cur_num != max_num + 1:
        if cur_num in nums_sets:
            count = count + 1
            if max_count < count:
                max_count = count
        else:
            count = 0
        cur_num = cur_num + 1

    return max_count

    # return type: integer
