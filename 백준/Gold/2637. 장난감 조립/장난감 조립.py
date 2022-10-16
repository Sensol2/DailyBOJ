from collections import deque
import math
import sys

input = sys.stdin.readline


def TopologicalSort():
    basic = []
    Q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            Q.append(i)
            basic.append(i)  # 기본 부품
    DP = [[0]*(N+1) for _ in range(N+1)]
    while Q:
        node = Q.popleft()
        for edge, parts in graph[node]:
            indegree[edge] -= 1

            if node in basic:
                DP[edge][node] = parts
            else:
                for i in range(len(DP[edge])):
                    DP[edge][i] += DP[node][i] * parts
            if indegree[edge] == 0:
                Q.append(edge)

    result = []
    for i in range(1, len(DP[N])):
        if i in basic:
            result.append([i, DP[N][i]])
    return result


N = int(input())
M = int(input())

graph = [[]*(N+1) for _ in range(N+1)]
indegree = [0]*(N+1)

for i in range(M):
    X, Y, K = map(int, input().split())
    indegree[X] += 1
    graph[Y].append([X, K])


dp = TopologicalSort()

for i in dp:
    print(i[0], i[1])
