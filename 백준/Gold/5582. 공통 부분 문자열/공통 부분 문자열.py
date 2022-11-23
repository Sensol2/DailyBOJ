import sys
input = sys.stdin.readline

A = list(input().rstrip())
B = list(input().rstrip())

DP = [[0] * (len(A)+1) for _ in range(len(B)+1)]
max_length = 0
for i in range(1, len(B)+1):
    for j in range(1, len(A)+1):
        if A[j-1] == B[i-1]:
            DP[i][j] = DP[i-1][j-1] + 1
        if max_length < DP[i][j]:
            max_length = DP[i][j]
print(max_length)
