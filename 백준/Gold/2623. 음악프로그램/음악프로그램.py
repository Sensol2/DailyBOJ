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
        for edge in graph[node]:
            indegree[edge] -= 1
            if indegree[edge] == 0:
                Q.append(edge)
    return result


N, M = map(int, input().split())
graph = [[]*(N+1) for _ in range(N+1)]
indegree = [0]*(N+1)
for i in range(M):
    arr = list(map(int, input().split()))
    arr = arr[1:]
    for j in range(len(arr)):
        for k in range(j+1, len(arr)):
            graph[arr[j]].append(arr[k])
            indegree[arr[k]] += 1

res = TopologicalSort()
if len(res) != N:
    print(0)
else:
    for i in res:
        print(i)
