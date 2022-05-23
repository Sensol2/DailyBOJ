import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

DP = [0] * N
DP[0] = arr[0]
for i in range(1, N):
    DP[i] = DP[i-1] + arr[i]


for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    if a == 0:
        print(DP[b])
    else:
        print(DP[b]-DP[a-1])
