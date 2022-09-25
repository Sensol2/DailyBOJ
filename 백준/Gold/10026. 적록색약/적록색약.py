from collections import deque


def BFS(x, y, visited, mode):
    # 상, 하, 좌, 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    color = graph[y][x]
    RGCweakness = mode

    Q = deque()
    Q.append([x, y])
    visited[y][x] = True

    count = 1
    while Q:
        x, y = Q.pop()
        count += 1
        for i in range(4):
            ty = dy[i] + y
            tx = dx[i] + x

            if tx < 0 or ty < 0 or tx >= N or ty >= N:
                continue

            if graph[ty][tx] != color:
                if not (RGCweakness and color in ['R', 'G'] and graph[ty][tx] in ['R', 'G']):
                    continue

            if not visited[ty][tx]:
                visited[ty][tx] = True
                Q.append([tx, ty])
    return count


N = int(input())
graph = [[]*N for _ in range(N)]
visited = [[False]*N for _ in range(N)]
for i in range(N):
    graph[i] = list(input())

# 적록색약 아닌 경우
res = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(j, i, visited, False)
            res += 1
print(res, end=' ')

# 적록색약인 경우
visited = [[False]*N for _ in range(N)]
res = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(j, i, visited, True)
            res += 1
print(res, end=' ')
