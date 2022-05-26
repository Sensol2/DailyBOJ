import math
import sys
import heapq


input = sys.stdin.readline
N, M = map(int, input().split())
K = int(input())

adj = [[]*(N+1) for _ in range(N+1)]
for i in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

Q = []
Q.append((K, 0))

visisted = [False] * (N+1)
visisted[K] = True

res = [math.inf] * (N+1)  # 최소 비용 리스트
res[K] = 0  # 시작점 자기 자신은 0
heap = []
while Q:
    item = Q.pop()
    node, currCost = item[0], item[1]

    for item in adj[node]:  # 인접 노드 중
        dest, cost = item[0], item[1]

        if res[dest] > cost + currCost:  # 더 빠른 경로가 있으면 update
            res[dest] = cost + currCost
            heapq.heappush(heap, (res[dest], dest))

    next_node = None
    while heap:
        if not visisted[heap[0][1]]:
            accumulated = heap[0][0]
            next_node = heap[0][1]
            break
        else:
            heapq.heappop(heap)

    if next_node:
        # 가는 경로로 가는 cost + 지금까지 오는 데 걸린 cost
        Q.append((next_node, accumulated))
        visisted[next_node] = True

for i in range(1, len(res)):
    if res[i] == math.inf:
        print("INF")
    else:
        print(res[i])
