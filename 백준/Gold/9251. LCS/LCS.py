str1 = input()
str2 = input()

M = len(str1) + 1
N = len(str2) + 1
DP = [[0]*(M) for _ in range(N)]
max_value = -1
for i in range(N):
    for j in range(M):
        if i == 0 or j == 0:
            DP[i][j] = 0
            continue
        if str2[i-1] == str1[j-1]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])

        if max_value < DP[i][j]:
            max_value = DP[i][j]
print(max_value)
