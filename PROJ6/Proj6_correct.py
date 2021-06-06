def P1(num):
    cnt = 0
    # num = 1...100...0
    # num-1 = 1...011...1
    # nun & (num-1) = 1...000...0
    # num & (num-1)을 하면 가장 오른쪽의 1 이 0 으로 됨
    # num 이 0 이 될 때까지 반복하면 1 의 개수를 셀 수 있음
    while num:
        num &= num - 1
        cnt += 1
    return cnt


def P2(x, y):
    cnt = 0
    num = x ^ y
    # XOR 을 하면 같은 bit 는 0 이 되고, 다른 bit 는 1 이 됨
    # P1 을 이용해서 1 의 개수를 셈
    while num:
        num &= (num-1)
        cnt += 1
    return cnt


def P3_ans(num):
    ans = 0
    # ans 를 1 bit right shfit 하고 LSB 를 더하는 작업을 반복
    for _ in range(32):
        ans = (ans << 1) + (num & 1)
        num >>= 1
    return ans


def P4_ans(nums):
    xor = 0
    # XOR 의 성질
    # 1. commutative
    # 2. A XOR A = 0
    # 즉, nums 에 있는 것을 모두 XOR 하면 찾고 싶은 두 수를 XOR 한 값과 같음
    for i in nums:
        xor ^= i
    # 찾고 싶은 두 수는 서로 다르기 때문에 xor 은 0 이 아니고, bit 가 1 인 자리는 두 수의 bit 가 다른 자리들.
    # 이 중에 아무거나 하나만 고를 것임 (가장 오른쪽 1 을 고를 것임. 다음과 같이 간단하게 구할 수 있으므로)
    # xor & (xor-1) 을 하면 가장 오른쪽의 1 이 0 이 되고,
    # 거기에 xor 과 다시 XOR 을 하면 xor & (xor-1) 에서 0 이된 1 만 살아남음
    # 즉, nonzero 는 100...0 이런 값
    nonzero = xor & (xor-1) ^ xor
    # num1 은 찾고 싶은 두 수 중 하나
    num1 = 0
    # nums 에 있는 수를 두 분류로 나눌 수 있음
    # 1. nonzero 자리의 bit 가 1 인 수들
    # 2. nonzero 자리의 bit 가 0 인 수들
    # 그리고 찾고 싶은 두 수는 각각 1 번에 하나 2 번에 하나가 있음
    # 따라서 1 번 부류의 수들을 모두 XOR 하면 하나를 찾을 수 있음(중복된 수들은 XOR 하면 0)
    for i in filter(lambda n: n & nonzero, nums):
        num1 ^= i
    # 나머지 하나는 2 번 부류를 모두 XOR 해도 되지만 xor 이랑 찾은 수랑 XOR 해도 됨
    return set({num1, xor ^ num1})
