"""
Same explanation with P8 (sparse vector)

The dot product of two vectors is the sum of the products of corresponding elements. 
For example, the dot product of [1, 2, 3] and [4, 5, 6] is 4+10+18 = 32. 
Implement another function that calculates the dot product of two sparse vectors.


>>>P9({0:1, 6:3}, {0:2, 5:2, 6:2, 7:1})
8

>>>P9({0:1, 6:3}, {1:-1, 2:2, 3:2, 4:1})
0

>>>P9({0:1, 6:-3}, {0:-1, 6:3})
-10
"""


def P9(dct1, dct2):

    def dictToVector(dct):
        vector = []
        keyList = []

        for key in dct:
            keyList.append(key)

        keyList.sort()

        for i in range(keyList[-1] + 1):
            if i in keyList:
                vector.append(dct[i])
            else:
                vector.append(0)

        return vector

    def dotVector(v1, v2):  # allow the difference in lengths of two vectors
        result = []

        while len(v1) != 0 and len(v2) != 0:
            result.append(v1.pop(0) * v2.pop(0))

        return result

    result = sum(dotVector(dictToVector(dct1), dictToVector(dct2)))

    return result
