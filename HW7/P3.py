def P3(matrix):
    width = len(matrix[0])
    height = len(matrix)
    element_dict = {}
    result = []

    for i in range(-width + 1, height):
        element_dict[i] = []

    for i in range(height):
        result.append([0] * width)

    for row_num in range(height):
        for col_num in range(width):
            element_dict[row_num - col_num].append(matrix[row_num][col_num])

    for i in range(-width + 1, height):
        element_dict[i].sort()
        if i <= 0:
            for j in range(len(element_dict[i])):
                result[j][j - i] = element_dict[i][j]
        else:
            for j in range(len(element_dict[i])):
                result[i + j][j] = element_dict[i][j]

    return result
