N, K = map(int, input().split())

DP = [[0] * (N+1) for _ in range(K+1)]
DP[1] = [1] * (N+1)
for i in range(2, K+1):
    for j in range(N+1):
        if j == 0:
            DP[i][j] = 1
            continue

        DP[i][j] = (DP[i][j-1] + DP[i-1][j]) % 1000000000
print(DP[K][N])
