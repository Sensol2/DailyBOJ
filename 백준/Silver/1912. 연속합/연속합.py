N = int(input())
arr = []
arr = list(map(int, input().split()))

DP = [0] * N
DP[0] = arr[0]

for i in range(1, len(arr)):
    DP[i] = max([DP[i-1] + arr[i], arr[i-1] + arr[i], arr[i]])

print(max(DP))
