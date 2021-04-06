def P5(lst):
    cur_num = 1
    successive_nums_max = 0

    while cur_num <= len(lst):
        successive_nums = 0
        for i in lst:
            if i == cur_num:
                successive_nums += 1
                cur_num += 1
        if successive_nums > successive_nums_max:
            successive_nums_max = successive_nums

    min_act = len(lst) - successive_nums_max
    return min_act
