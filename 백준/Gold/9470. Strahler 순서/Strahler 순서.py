from collections import deque
import sys

input = sys.stdin.readline


def topologicalSort():
    result = []
    strahler = [[] for _ in range(M+1)]
    Q = deque()
    for i in range(1, M+1):
        if indegree[i] == 0:
            Q.append([i, 1])

    while Q:
        node, depth = Q.popleft()
        result.append([node, depth])

        for edge in graph[node]:
            indegree[edge] -= 1
            strahler[edge].append(depth)
            if indegree[edge] == 0:
                i = max(strahler[edge])
                if strahler[edge].count(i) == 1:
                    next = i
                if strahler[edge].count(i) >= 2:
                    next = i+1
                Q.append([edge, next])

    return result


T = int(input())
for i in range(T):
    K, M, P = map(int, input().split())
    graph = [[]*(M+1) for _ in range(M+1)]
    indegree = [0]*(M+1)

    for j in range(P):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    res = topologicalSort()

    print(K, res[M-1][1])
