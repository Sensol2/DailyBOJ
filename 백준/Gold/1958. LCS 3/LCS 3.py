str1 = input()
str2 = input()
str3 = input()

A = len(str1) + 1
B = len(str2) + 1
C = len(str3) + 1

DP = [[[0]*A for _ in range(B)]for _ in range(C)]
max_value = -1
for i in range(C):
    for j in range(B):
        for k in range(A):
            if i == 0 or j == 0 or k == 0:
                DP[i][j][k] = 0
                continue
            if str1[k-1] == str2[j-1] and str2[j-1] == str3[i-1]:
                DP[i][j][k] = DP[i-1][j-1][k-1] + 1
            else:
                DP[i][j][k] = max(
                    DP[i-1][j][k], max(DP[i][j-1][k], DP[i][j][k-1]))
            if max_value < DP[i][j][k]:
                max_value = DP[i][j][k]
print(max_value)
