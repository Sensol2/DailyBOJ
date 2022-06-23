import math

N = int(input())
street = [[0]*3 for _ in range(N+1)]
DP = [[[0]*3 for _ in range(N+1)] for _ in range(3)]

for i in range(1, N+1):
    street[i] = list(map(int, input().split()))

for i in range(3):
    DP[i][0] = [0, 0, 0]
    DP[i][1] = street[1]

for i in range(3):
    for j in range(2, N+1):
        for k in range(3):
            min_arr = []

            if j == 2:
                if i == k:
                    DP[i][j][k] = math.inf
                else:
                    DP[i][j][k] = street[j-1][i] + street[j][k]
                continue

            if j == N and i == k:
                DP[i][j][k] = math.inf
                continue

            for l in range(3):
                if k != l:
                    min_arr.append(DP[i][j-1][l])
            DP[i][j][k] = min(min_arr) + street[j][k]

print(min(DP[0][N] + DP[1][N] + DP[2][N]))
