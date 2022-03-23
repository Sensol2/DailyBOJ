N, M = map(int, input().split())

maze = [[] for _ in range(N)]
visited = [[False]*M for _ in range(N)]
visited[0][0] = True
for i in range(N):
    maze[i] = list(map(int, list(input())))

x = 0
y = 0
queue = [[y,x]]
# 동, 남, 서, 북
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

while queue:
    y = queue[0][0]
    x = queue[0][1]
    queue.pop(0)

    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]

        if ty < 0 or ty >= N or tx < 0 or tx >= M:
            continue
        if maze[ty][tx] == 0:
            continue
        else:
            if visited[ty][tx] == False:
                visited[ty][tx] = True
                maze[ty][tx] = maze[y][x] + 1
                queue.append([ty, tx])
print(maze[N-1][M-1])