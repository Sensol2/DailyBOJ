import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0] * N for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

DP = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if j == 0:
            DP[i][j] = arr[i][j]
        else:
            DP[i][j] = DP[i][j-1] + arr[i][j]

# 입력부
for i in range(M):
    y1, x1, y2, x2 = map(lambda x: x-1, map(int, input().split()))
    result = 0
    for j in range(y1, y2+1):  # 행 이동하면서
        if x1 == 0:
            result += DP[j][x2]
        else:
            result += DP[j][x2] - DP[j][x1-1]
    print(result)