def GeneratePrefixSum(arr):
    size = len(arr)
    DP = [0] * size
    DP[0] = arr[0]
    for i in range(1, size):
        DP[i] = DP[i-1] + arr[i]
    return DP


def GetPrefixSum(DP, start, end):
    DP = [0] + DP  # margin
    return DP[end] - DP[start-1]


T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

DP_A = GeneratePrefixSum(A)
DP_B = GeneratePrefixSum(B)
DICT_A = dict()
DICT_B = dict()

for i in range(1, n+1):
    for j in range(i, n+1):
        res = GetPrefixSum(DP_A, i, j)
        if res in DICT_A.keys():
            DICT_A[res] += 1
        else:
            DICT_A[res] = 1

for i in range(1, m+1):
    for j in range(i, m+1):
        res = GetPrefixSum(DP_B, i, j)
        if res in DICT_B.keys():
            DICT_B[res] += 1
        else:
            DICT_B[res] = 1

count = 0
for sum_a in DICT_A.keys():
    if (T-sum_a) in DICT_B.keys():
        count += DICT_A[sum_a] * DICT_B[T-sum_a]
print(count)
