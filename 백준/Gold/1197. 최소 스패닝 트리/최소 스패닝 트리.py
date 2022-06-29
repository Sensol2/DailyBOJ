import heapq
from queue import PriorityQueue
import sys

input = sys.stdin.readline

V, E = map(int, input().split())


graph = [[] for _ in range(V+1)]
visited = [False]*(V+1)
visited[0] = True

heap = []
for i in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((A, B, C))
    graph[B].append((B, A, C))

start = 1  # 시작 정점을 1로 설정
visited[1] = True
for v in graph[start]:
    start, end, cost = v[0], v[1], v[2]
    heapq.heappush(heap, (cost, (start, end)))

result = 0
while heap:
    item = heapq.heappop(heap)
    start, end, cost = item[1][0], item[1][1], item[0]

    if visited[start] and visited[end]:  # 둘 다 방문한 경우
        continue
    if not visited[start] and not visited[end]:  # 둘 다 방문하지 않은 경우
        continue
    else:
        visited[start] = True
        visited[end] = True
        result += cost

        for v in graph[end]:
            start, end, cost = v[0], v[1], v[2]
            heapq.heappush(heap, (cost, (start, end)))
print(result)
