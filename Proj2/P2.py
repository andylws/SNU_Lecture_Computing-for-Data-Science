"""
**Instruction**
Please see instruction document.

"""


def P2(parentheses: str) -> bool:
    ##### Write your Code Here #####
    par_list = ['.']

    for i in parentheses:
        if i == '(' or i == '{' or i == '[':
            par_list.append(i)
        elif i == ')':
            if par_list[-1] == '(':
                par_list.pop()
            else:
                return False
        elif i == '}':
            if par_list[-1] == '{':
                par_list.pop()
            else:
                return False
        elif i == ']':
            if par_list[-1] == '[':
                par_list.pop()
            else:
                return False

    if par_list == ['.']:
        return True
    else:
        return False
    ##### End of your code #####
