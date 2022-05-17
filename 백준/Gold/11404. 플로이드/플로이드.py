import math
import sys
n = int(input())
m = int(input())
cost = [[math.inf]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    cost[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    if cost[a][b] > c:
        cost[a][b] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if cost[i][j] > cost[i][k] + cost[k][j]:
                cost[i][j] = cost[i][k] + cost[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if cost[i][j] == math.inf:
            print(0, end=' ')
        else:
            print(cost[i][j], end=' ')
    print()
