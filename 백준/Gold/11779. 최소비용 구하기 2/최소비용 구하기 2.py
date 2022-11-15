import math
import heapq
import sys
input = sys.stdin.readline


def dijkstra(start):
    Q = [[0, start]]
    while Q:
        dist, now = heapq.heappop(Q)  # dist: 현재까지의 누적거리

        if dist > distance[now]:  # 기록된 최단경로보다 비효율적이면 패스
            continue

        for next, cost in graph[now]:
            if dist + cost < distance[next]:
                distance[next] = dist + cost
                heapq.heappush(Q, [dist + cost, next])
                nearestNode[next] = now


N = int(input())
M = int(input())
graph = [[] * (N+1) for _ in range(N+1)]
distance = [math.inf] * (N+1)


for i in range(M):
    s, e, c = map(int, input().split())
    graph[s].append([e, c])
src, dest = map(int, input().split())
nearestNode = [src] * (N+1)
dijkstra(src)

result = []
node = dest
while node != src:  # 뒤에서부터 역추적
    result.append(node)
    node = nearestNode[node]
result.append(src)
result = list(reversed(result))
print(distance[dest])
print(len(result))
print(" ".join(map(str, result)))
