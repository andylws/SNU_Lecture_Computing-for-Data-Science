"""
Implement a function that takes two dictionaries as arguments
and returns a dictionary that contains only the key/value pairs found in both
of the original dictionaries.


>>> P5({'a': 1, 'b':True, 'c':[1,2]}, {'a':1, 'b':123, 'c':[1,2]})
{'a': 1, 'c': [1, 2]}

>>> P5({'a': 1, 'b':True }, {'c':1, 'd':123, 'e':[1,2]})
{}

>>> P5({}, {'c':1, 'd':123, 'e':[1,2]})
{}

"""


def P5(dct1, dct2):
    interKeys = dct1.keys() & dct2.keys()
    result = {}

    for key in interKeys:
        if dct1[key] == dct2[key]:
            result[key] = dct1[key]

    return result
