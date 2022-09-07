from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def DFS(graph, nodeIdx, parentIdx):
    visited[nodeIdx] = True  # 방문처리

    for node in graph[nodeIdx]:
        if not visited[node]:
            DFS(graph, node, nodeIdx)

    if parentIdx:  # root가 아닐때
        if not EA[nodeIdx]:
            EA[parentIdx] = True


N = int(input())
graph = [[]*(N+1) for _ in range(N+1)]
EA = [False] * (N+1)  # Early Adapter
visited = [False] * (N+1)

for i in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

DFS(graph, 1, None)
print(EA.count(True))
