def P4(A, B):
    L = len(A)
    S = 0

    A.sort()
    B.sort(reverse=True)

    for i in range(L):
        S = S + A[i] * B[i]

    return S
