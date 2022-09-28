import math
import heapq


def prim(graph, start):
    visited[start] = True

    candidate = graph[start]
    heapq.heapify(candidate)

    total_cost = 0

    while candidate:
        c, v = heapq.heappop(candidate)
        if not visited[v]:
            visited[v] = True
            total_cost += c

            for edge in graph[v]:
                next_node = edge[1]
                if not visited[next_node]:
                    heapq.heappush(candidate, edge)

    return total_cost


N = int(input())
M = int(input())

graph = [[]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])
print(prim(graph, 1))
