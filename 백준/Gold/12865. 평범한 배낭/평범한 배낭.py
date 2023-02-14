import sys

input = sys.stdin.readline

N, K = map(int, input().split())
item = [[0, 0]]*(N+1)
for i in range(N):
    w, v = map(int, input().split())
    item[i] = [w, v]

item = sorted(item, key=lambda x: x[0])
DP = [[0] * (N+1) for _ in range(K+1)]

result = 0
for i in range(K+1):  # 최대 무게
    for j in range(N+1):  # 아이템 인덱스
        if i == 0 and j == 0:
            continue
        elif item[j][0] > i:  # 용량초과
            DP[i][j] = DP[i][j-1]
        else:
            DP[i][j] = max(item[j][1] + DP[i-item[j][0]][j-1], DP[i][j-1])

        if DP[i][j] > result:
            result = DP[i][j]
print(result)
