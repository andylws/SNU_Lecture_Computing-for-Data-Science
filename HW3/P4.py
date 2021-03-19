"""
Practical programming Chapter 9 Exercise 11

**Instruction**
Inputs are two integers start_i, end_i. (start_i < end_i)
This function sums all integers between start_i and end_i(both inclusive), 
then calculate average of these integers using loop.
Complete P4 function. 

P4(2, 22)
>>> 12

P4(0, 100)
>>> 50

"""


def P4(start_i: int, end_i: int) -> float:
    ##### Write your Code Here #####

    sum_between = 0
    for i in range(start_i, end_i + 1):
        sum_between = sum_between + i
    avg = sum_between / (end_i - start_i + 1)

    return avg

    ##### End of your code #####
