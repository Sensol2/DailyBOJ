from collections import deque
import sys

input = sys.stdin.readline


def TopologicalSort():

    result = []
    Q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            Q.append(i)

    while Q:
        node = Q.popleft()
        result.append(node)
        for i in range(1, N+1):
            if graph[node][i] == 0:
                continue
            # 간선 제거
            graph[node][i] = 0
            indegree[i] -= 1
            if indegree[i] == 0:
                Q.append(i)

    return result


def ReverseEdge(a, b):
    # reverse: a<->b
    graph[a][b] = 0
    graph[b][a] = 1
    indegree[b] -= 1
    indegree[a] += 1


T = int(input())

for t in range(T):
    N = int(input())
    graph = [[0]*(N+1) for _ in range(N+1)]
    indegree = [0]*(N+1)
    rank = [0] + list(map(int, input().split()))
    # [0] : margin
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            graph[rank[i]][rank[j]] = 1  # i->j
            indegree[rank[j]] += 1

    M = int(input())
    for m in range(M):
        a, b = map(int, input().split())
        if graph[a][b] == 1:  # -> to <-
            ReverseEdge(a, b)
        elif graph[b][a] == 1:
            ReverseEdge(b, a)

    res = TopologicalSort()
    if len(res) != N:
        print("IMPOSSIBLE")
    else:
        print(' '.join(map(str, res)))
