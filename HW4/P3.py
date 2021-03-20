"""
Implement a function that takes a dictionary as an argument
and returns the number of values that appear two or more times.

* Condition: All values are hashable.


>>> P3({'red': 1, 'green': 1, 'blue': 2})
1

>>> P3({'r': 'a', 'g': 'b', 'b': 'c'})
0

>>> P3(dict())
0

>>> P3({'a':True, 'b': True, 'c':2, 'd':2})
2
"""


def P3(dct):
    '''
    ## First Solution ##

    temp_set = set()
    tempList = []
    result = set()

    for i in dct:
        temp_set.add(dct[i])
        tempList.append(dct[i])

    for i in tempList:
        if i in temp_set:
            temp_set.remove(i)
        else:
            result.add(i)

    return len(result)

    '''

    ########################################

    ''' ## Second Solution ## '''

    tempList = []
    result = set()

    for key in dct:
        if dct[key] in tempList:
            result.add(dct[key])
        else:
            tempList.append(dct[key])

    return len(result)
