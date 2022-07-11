N = int(input())
arr = []

arr = list(map(int, input().split()))
DP = [1] * N

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            DP[i] = max(DP[i], DP[j] + 1)

print(max(DP))
