N = int(input())
arr = []

arr = list(map(int, input().split()))
DP = [1] * N
DP_SET = [[x] for x in arr]
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            if DP[i] < DP[j] + 1:
                DP_SET[i] = DP_SET[j] + [arr[i]]
            DP[i] = max(DP[i], DP[j] + 1)
print(max(DP))
print(' '.join(map(str, DP_SET[DP.index(max(DP))])))
