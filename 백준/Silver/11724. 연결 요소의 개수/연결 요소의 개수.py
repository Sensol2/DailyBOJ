from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        count += 1
        Q = deque()
        Q.append(i)
        while Q:
            item = Q.pop()
            nodes = graph[item]
            for node in nodes:
                if not visited[node]:
                    visited[node] = True
                    Q.append(node)

print(count)
