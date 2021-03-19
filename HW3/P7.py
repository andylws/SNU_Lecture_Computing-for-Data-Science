"""
Practical programming Chapter 8 Exercise 10

**Instruction**
Inputs are a nested list having two lists. 
Complete P7 function that returns a list whose elements are as following:
- the list has 2 items
- the first item is the first item of the first inner list of input
- the second item is the last item of the second inner list of input

P7([['km','miles','league'],['kg','pound','stone']])
>>> ['km','stone']

P7([[0,1,2,3],[4,5,6]])
>>> [0,6]

P7([[0,0,0],[1]])
>>> [0,1]
"""


def P7(nested_list: list) -> list:
    ##### Modify code Here #####

    result = []
    result.append(nested_list[0][0])
    result.append(nested_list[1][-1])

    return result

    ##### End of your code #####
