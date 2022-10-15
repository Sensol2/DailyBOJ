from collections import deque
import heapq
import sys
input = sys.stdin.readline


def TopologicalSort():
    result = []
    heap = []

    for i in range(1, N+1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)

    while heap:
        node = heapq.heappop(heap)
        result.append(node)
        for edge in graph[node]:
            indegree[edge] -= 1  # 진입차수 1 감소
            if indegree[edge] == 0:
                heapq.heappush(heap, edge)
    return result


N, M = map(int, input().split())
graph = [[] * (N+1) for _ in range(N+1)]
indegree = [0] * (N+1)
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

res = TopologicalSort()
print(' '.join(map(str, res)))
