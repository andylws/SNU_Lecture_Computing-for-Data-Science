"""
#Practical programming Chapter 9 Exercise 3

**Instruction**
Write a function that uses for loop to add 1 to all the values from input list 
and return the new list. The input list shouldn’t be modified. 
Assume each element of input list is always number.
Complete P3 function

P3([5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3])
>>> [6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2, 4]

P3([0,0,0])
>>> [1,1,1]

"""


def P3(L1: list) -> list:
    ##### Write your Code Here #####

    result = []
    for i in L1:
        result.append(i + 1)

    return result

    ##### End of your code #####
