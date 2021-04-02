def P1(lst):
    current_swap = 1
    total_swap = 0

    while current_swap != 0:
        current_swap = 0
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                total_swap = total_swap + 1
                current_swap = current_swap + 1

    return total_swap
