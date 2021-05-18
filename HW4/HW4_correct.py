def P1_ans(lst):
    origin = set()
    ans = set()
    for i in lst:
        if i in origin:
            ans.add(i)
        else:
            origin.add(i)
    return ans


def P2_ans(dct):
    return len(set(dct.values()))


def P3_ans(dct):
    ans = set()
    origin = set()
    for i in dct:
        if dct[i] in origin:
            ans.add(dct[i])
        else:
            origin.add(dct[i])
    return len(ans)


def P4_ans(dct):
    return sum(dct.values()) == 1.0


def P5_ans(dct1, dct2):
    ans = dict()
    for i in dct1:
        if i in dct2:
            if dct1[i] == dct2[i]:
                ans[i] = dct1[i]
    return ans


def P6_ans(dct):
    ans = set()
    for i in dct:
        ans = ans.union(set(dct[i].keys()))
    return ans


def P7_ans(dct):
    keys = None
    for i in dct:
        if keys == None:
            keys = set(dct[i].keys())
        else:
            if set(dct[i].keys()) != keys:
                return False
    return True


def P8_ans(dct1, dct2):
    ans = dict()
    for i in dct1:
        if i not in dct2:
            ans[i] = dct1[i]
        else:
            if dct1[i] + dct2[i] != 0:
                ans[i] = dct1[i] + dct2[i]
    for i in dct2:
        if i not in dct1:
            ans[i] = dct2[i]
    return ans


def P9_ans(dct1, dct2):
    ans = 0
    for i in dct1:
        if i in dct2:
            ans += dct1[i] * dct2[i]
    return ans


def P10_ans(word_set, query_word):
    for cand in word_set:
        if len(cand) == len(query_word):
            diff = 0
            for i in range(len(cand)):
                if cand[i] != query_word[i]:
                    diff += 1
            if diff == 1:
                return True
    return False
