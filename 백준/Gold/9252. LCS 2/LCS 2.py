def LCS(i, j, stack):
    if DP[i][j] == 0:
        while stack:
            print(stack.pop(), end='')
        return
    if DP[i][j] == DP[i-1][j]:
        LCS(i-1, j, stack)
    elif DP[i][j] == DP[i][j-1]:
        LCS(i, j-1, stack)
    else:
        stack.append(str1[j-1])
        LCS(i-1, j-1, stack)


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
LCS(N-1, M-1, [])
# LCS
# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence
