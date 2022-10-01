import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

order = 1


def DFS(graph, node):
    global order
    priority[node] = order

    if not graph[node]:
        return

    for n in graph[node]:
        if not visited[n]:
            visited[n] = True
            order += 1
            DFS(graph, n)


N, M, R = map(int, input().split())

graph = [[]*(N+1) for _ in range(N+1)]
visited = [False] * (N+1)
priority = [0] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 인접 정점 오름차순 정렬
for i in range(N):
    graph[i] = sorted(graph[i])

visited[R] = True

DFS(graph, R)
for p in range(1, N+1):
    print(priority[p])
