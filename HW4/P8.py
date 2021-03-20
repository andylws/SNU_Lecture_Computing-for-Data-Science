"""
A sparse vector is a vector whose entries are almost all zero, like [1, 0, 0, 0, 0, 0, 3, 0, 0, 0]. 
Storing all those zeros in a list wastes memory, so programmers often use dictionaries instead 
to keep track of just the nonzero entries. For example, the vector shown earlier would be 
represented as {0:1, 6:3}, because the vector it is meant to represent has 
the value 1 at index 0 and the value 3 at index 6.

The sum of two vectors is just the element-wise sum of their elements.
For example, the sum of [1, 2, 3] and [4, 5, 6] is [5, 7, 9]. Implement a function
that takes two sparse vectors stored as dictionaries and returns a new dictionary representing their sum.

* Condition: All entries of vector are integers.


>>> P8({0:1, 6:3}, {0:2, 5:2, 6:2, 7:1})
{0:3, 5:2, 6:5, 7:1}

>>> P8({0:1, 6:3}, {0:-1, 5:2, 6:2, 7:1})
{6: 5, 5: 2, 7: 1}

>>> P8({0:1, 6:3}, {0:-1, 1:1, 2:2, 6:-3})
{1: 1, 2: 2}

>>> P8({0:1, 6:-3}, {0:-1, 6:3})
{}
"""


def P8(dct1, dct2):
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

    def sumVector(v1, v2):
        resultVector = []

        while len(v1) * len(v2) != 0:
            resultVector.append(v1.pop(0) + v2.pop(0))

        resultVector = resultVector + v1 + v2

        return resultVector

    def vectorToDict(v):
        resultDict = {}

        for i in range(len(v)):
            if v[i] != 0:
                resultDict[i] = v[i]
            else:
                continue

        return resultDict

    vector1 = dictToVector(dct1)
    vector2 = dictToVector(dct2)

    result = vectorToDict(sumVector(vector1, vector2))

    return result
