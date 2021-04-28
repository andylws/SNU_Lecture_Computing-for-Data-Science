def P4(nums):
    # nums: list of int
    result = set()

    for i in nums:
        if i not in result:
            result.add(i)
        else:
            result.remove(i)

    return result

    # return type: set
