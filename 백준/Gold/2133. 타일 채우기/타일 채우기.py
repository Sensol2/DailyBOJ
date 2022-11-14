N = int(input())
DP = [0] * (31)
DP[0] = 1
DP[2] = 3
DP[4] = 11

for i in range(6, N+1, 2):
    DP[i] = DP[i-2]*3 + sum(DP[0:i-2]) * 2

print(DP[N])
