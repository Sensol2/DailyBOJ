N = int(input())
K = int(input())

link = [[] for _ in range(N+1)]

for i in range(K):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

infected = 0
visited = [False] * (N+1)
queue = []
queue.append(1)
while queue:
    currNode = queue.pop(0)
    if visited[currNode] == True:
        continue

    infected += 1
    visited[currNode] = True
    for i in link[currNode]:
        queue.append(i)
    
print(infected - 1)