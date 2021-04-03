def P2(lst):
    def merge(input_list, first, mid, last):
        sub_list1 = input_list[first: mid + 1]
        sub_list2 = input_list[mid + 1: last + 1]
        i = 0
        j = 0
        k = first

        while i < len(sub_list1) and j < len(sub_list2):
            if len(sub_list1[i]) == len(sub_list2[j]):
                if sub_list1[i] < sub_list2[j]:
                    input_list[k] = sub_list1[i]
                    i = i + 1
                else:
                    input_list[k] = sub_list2[j]
                    j = j + 1
            elif len(sub_list1[i]) <= len(sub_list2[j]):
                input_list[k] = sub_list1[i]
                i = i + 1
            else:
                input_list[k] = sub_list2[j]
                j = j + 1
            k = k + 1

        if i < len(sub_list1):
            input_list[k: last + 1] = sub_list1[i:]
        elif j < len(sub_list2):
            input_list[k: last + 1] = sub_list2[j:]

        print(lst)

    def mergeSortHelp(input_list, first, last):
        if first == last:
            return
        else:
            mid = (first + last) // 2
            mergeSortHelp(input_list, first, mid)
            mergeSortHelp(input_list, mid+1, last)
            merge(input_list, first, mid, last)

    def mergeSort(input_list):
        mergeSortHelp(input_list, 0, len(input_list) - 1)

    mergeSort(lst)

    return lst
