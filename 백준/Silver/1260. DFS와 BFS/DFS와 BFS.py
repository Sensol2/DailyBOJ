def DFS(field, visited, node):
    print(node, end=' ')
    visited[node] = True

    field[node].sort()
    for i in field[node]:
        if not visited[i]:
            DFS(field, visited, i)



N, M, V = map(int, input().split())

field = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    field[a].append(b)
    field[b].append(a)

visited = [False] * (N+1)
DFS(field, visited, V)

queue = [V]
visited = [False] * (N+1)
print()
while queue:
    index = queue.pop(0)
    print(index, end=' ')
    visited[index] = True

    field[index].sort()
    for i in field[index]:
        if visited[i] == False and i not in queue:
            queue.append(i)
    