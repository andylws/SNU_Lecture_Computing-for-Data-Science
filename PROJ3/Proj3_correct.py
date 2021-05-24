def P1(nums, k):
    # key: k로 나눈 나머지, value: k로 나눈 나머지가 key인 수의 개수
    freq = dict()
    for num in nums:
        if num % k in freq:
            freq[num % k] += 1
        else:
            freq[num % k] = 1
    for rem in freq:
        if rem == 0 or rem * 2 == k:
            if freq[rem] % 2 != 0:
                return False
        else:
            if k-rem not in freq:
                return False
            if freq[rem] != freq[k-rem]:
                return False
    return True


def P2(nums):
    first_cnt = dict()  # key: curr_cnt, value: curr_cnt값이 key인 가장 작은 index
    curr_cnt = 0  # 첫번째 부터 i번째 까지 "1의 개수" - "0의 개수"
    max_len = 0
    # nums[a:b]에서 1의 개수와 0의 개수가 같으면 nums[0:a]의 curr_cnt 값과 nums[0:b]의 curr_cnt 값이 같다는 점을 이용
    for i in range(len(nums)):
        if nums[i] == 0:
            curr_cnt += -1
        else:
            curr_cnt += 1
        if curr_cnt == 0:
            max_len = i+1
        else:
            if curr_cnt in first_cnt:
                max_len = max(max_len, i - first_cnt[curr_cnt])
            else:
                first_cnt[curr_cnt] = i
    return max_len


def P3(A, B):
    first_diff = dict()
    max_len = 0
    suma = 0
    sumb = 0
    first_diff[0] = -1
    # P2와 비슷하게, sum(A[x:y]) == sum(B[x:y]) 이면 sum(A[0:y]) - sum(A[0:x]) == sum(B[0:y]) - sum(A[0:x]) 인 점을 이용
    for i in range(len(A)):
        suma += A[i]
        sumb += B[i]
        diff = suma - sumb
        if diff not in first_diff:
            first_diff[diff] = i
        else:
            max_len = max(max_len, i-first_diff[diff])
    return max_len


def P4(nums):
    max_len = 0
    s = set(nums)
    # nums[i] 부터 1씩 증가시켜 가면서 연속인 것의 개수를 센다.
    # 이중 loop 이지만, if 문이 실행될 조건을 생각해 보면 O(n)인 것을 알 수 있다.
    for i in range(len(nums)):
        if nums[i] - 1 not in s:
            end = nums[i]
            while end in s:
                end += 1
            max_len = max(max_len, end - nums[i])
    return max_len
