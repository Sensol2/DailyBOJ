import math

N = int(input())
street = [[0]*3 for _ in range(N+1)]
DP = [[0]*3 for _ in range(N+1)]

for i in range(1, N+1):
    street[i] = list(map(int, input().split()))


DP[0] = [0, 0, 0]
DP[1] = street[1]
for i in range(2, N+1):
    for j in range(3):
        min_arr = []
        for k in range(3):
            if j != k:
                min_arr.append(DP[i-1][k])
        DP[i][j] = min(min_arr) + street[i][j]

print(min(DP[N]))
