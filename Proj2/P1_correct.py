"""
**Instruction**
Please see instruction document.

"""


def P1(path: str) -> str:
    ##### Write your Code Here #####
    path_list = []
    cur_dir = ''

    for char in path:
        if char != '/':
            cur_dir = cur_dir + char
        else:
            if cur_dir == '':
                continue
            elif cur_dir == '.':
                cur_dir = ''
                continue
            elif cur_dir == '..':
                if path_list == []:
                    cur_dir = ''
                    continue
                else:
                    path_list.pop()
            else:
                path_list.append(cur_dir)
            cur_dir = ''

    if not cur_dir in ['', '.', '..']:
        path_list.append(cur_dir)

    result_path = '/' + '/'.join(path_list)

    return result_path
    ##### End of your code #####
