"""
**Instruction**
<Factor into two prime numbers>
Input of P2 function is natural number.
P2 function returns whether the input number could be factored into two prime numbers.
Do not worry about invalid input.

>>> P2(6) #2 * 3
True

>>> P2(9) #3 * 3
True

>>> P2(12) # 2 * 2 * 3
False

>>> P2(7) # 7
False


"""


def P2(n: int) -> bool:
    ##### Write your Code Here #####
    '''
    First Solution

    def findDivisors(N):
        divisor_list = []

        for i in range(1, int(N + 1)):
            if N % i == 0:
                divisor_list.append(i)

        return divisor_list

    n_divisor_list = findDivisors(n)

    for divisor in n_divisor_list:
        couple = n / divisor
        divisor_divisor = findDivisors(divisor)
        couple_divisor = findDivisors(couple)
        if len(divisor_divisor) == 2 and len(couple_divisor) == 2:
            return True
        else:
            continue

    return False

    '''

    #######################################################

    ''' Second Solution '''

    current_n = n
    prime_factor_list = []

    for i in range(2, n):
        if n % i == 0:
            while current_n % i == 0:
                current_n = current_n / i
                prime_factor_list.append(i)

    if len(prime_factor_list) == 2:
        return True

    return False

    ##### End of your code #####
