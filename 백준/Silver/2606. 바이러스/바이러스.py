def dfs(graph, visited, node):
    if node in visited:
        return
    
    global count
    if node != 1:
        count += 1

    visited.add(node)
    
    for neighbour in graph[node]:
        dfs(graph, visited, neighbour)

N = int(input())
M = int(input())

count = 0
graph = [[] for _ in range(N+1)]
visited = set()

for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

dfs(graph, visited, 1)
print(count)