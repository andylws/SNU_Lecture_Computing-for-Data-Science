"""
There is a set of words and a query word.
You must change exactly one character of the query word.
Implement a function that determins whether the changed word can be the element of the set.

* Condition: Words consist of only lower-case alphabet(s) and no space.


>>> P10({"data", "science"}, "data")
False
Explanation: If you change one character of the query word, there is no matching word in the set.

>>> P10({"data", "science"}, "daaa")
True
Explanation: You can change one alphabet to make "daaa" -> "data" .

>>> P10({"data", "science"}, "scienzz")
False

>>> P10({"data", "science", "scienze"}, "scienzz")
True

>>> P10({"data", "science"}, "dataa")
False
"""


def P10(word_set, query_word):
    result = False

    for word in word_set:
        if len(word) != len(query_word):
            continue

        count = 0

        for i in range(len(word)):
            if word[i] == query_word[i]:
                continue
            else:
                count = count + 1
            if count > 1:
                break

        if count == 0:
            continue
        elif count == 1:
            result = True
            break
        else:
            continue

    return result
    # return type: boolean
