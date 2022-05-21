import math

N = int(input())
M = int(input())

matrix = [[math.inf] * (N+1) for _ in range(N+1)]
for i in range(M):
    f, t, c = map(int, input().split())
    if matrix[f][t] > c:
        matrix[f][t] = c

for i in range(N+1):
    for j in range(N+1):
        if i == j:
            matrix[i][j] = 0

start, dest = map(int, input().split())

arr = matrix[start]
visisted = [False] * (N+1)
Q = []
Q.append(start)
visisted[start] = True
while Q:
    i = Q.pop()
    currentCost = arr[i]
    for j in range(N+1):
        if arr[j] > matrix[i][j] + currentCost:
            arr[j] = matrix[i][j] + currentCost

    # 다음으로 비용 가장 적은 노드 탐색
    min_cost = math.inf
    next_node = None
    for j in range(N+1):
        if i == j:
            continue
        if min_cost > arr[j] and not visisted[j]:
            min_cost = arr[j]
            next_node = j
    if next_node:
        Q.append(next_node)
        visisted[next_node] = True
print(arr[dest])
