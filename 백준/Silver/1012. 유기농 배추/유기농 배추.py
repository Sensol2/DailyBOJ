from collections import deque

def BFS(farm, _x, _y, visited):
    my_queue = deque()
    my_queue.append([_x, _y])
    while my_queue:
        item = my_queue.pop()
        x, y = item[0], item[1]
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= M or ty < 0 or ty >= N:
                continue
            if farm[ty][tx] == 1 and not visited[ty][tx]:
                farm[ty][tx] = 2
                visited[ty][tx] = True
                my_queue.append([tx, ty])

T = int(input())

# 상, 하, 좌, 우
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
for i in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1

    visited = [[False] * M for _ in range(N)]
    count = 0
    for y in range(N):
        for x in range(M):
            if farm[y][x] == 1:
                BFS(farm, x, y, visited)
                count += 1
    print(count)
            