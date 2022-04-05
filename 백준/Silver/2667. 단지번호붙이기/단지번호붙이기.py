from collections import deque

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def DFS(graph, _y, _x, visited):
    count = 0
    my_queue = deque()
    my_queue.append([_y, _x])

    visited[_y][_x] = True
    while my_queue:
        item = my_queue.popleft()
        y, x = item[0], item[1]
        count += 1
        graph[y][x] = 0
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if tx < 0 or tx >= N or ty < 0 or ty >= N:
                continue
            else:
                if graph[ty][tx] != 0 and not visited[ty][tx]:
                    visited[ty][tx] = True
                    my_queue.append([ty, tx])
    return count

N = int(input())

graph = [None] * N
visited = [[False] * N for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, list(input())))

danji = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            danji.append(DFS(graph, i, j, visited))
if danji:
    danji.sort()
    print(len(danji))
    for i in danji:
        print(i)
if not danji:
    print(0)