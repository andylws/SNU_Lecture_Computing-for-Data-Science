"""
Implement a function that takes a single dictionary as an argument
and returns the number of distinct values it contains.

* Condition: All values are hashable.


>>> P2({'red': 1, 'green': 1, 'blue': 2})
2

>>> P2({(1,2): 'a', 'g': 3, 1: True})
3

>>> P2(dict())
0

>>> P2({'a':True, 'b': True, 'c':True})
1
"""


def P2(dct):
    '''
    ## First Solution ##

    result_list = []

    for i in dct:
        if dct[i] in result_list:
            continue
        else:
            result_list.append(dct[i])

    return len(result_list)

    '''

    #############################################

    ''' ## Second Solution ## '''

    result = set()

    for key in dct:
        result.add(dct[key])

    return len(result)
