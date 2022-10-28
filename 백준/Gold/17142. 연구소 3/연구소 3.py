from collections import deque
import math

# 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(virus):

    visited = [[False]*N for _ in range(N)]
    Q = deque()
    for x, y in virus:  # depth 추가
        visited[y][x] = True
        Q.append([x, y, 0])
    safearea = sum(x.count(0) for x in maze)
    if safearea == 0:
        return 0
    while Q:
        x, y, d = Q.popleft()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or ty < 0 or tx >= N or ty >= N:
                continue

            if maze[ty][tx] == 1:
                continue

            if not visited[ty][tx]:
                if maze[ty][tx] == 0:
                    safearea -= 1  # 안전지대 개수 1개 감소
                    if safearea <= 0:
                        return d + 1
                visited[ty][tx] = True
                Q.append([tx, ty, d+1])

    return -1


results = []


def setVirus(arr, idx):

    if len(arr) > M:
        return
    if len(arr) == M:
        results.append(bfs(arr))
        # 탐색
        return

    for i in range(idx, len(virusPos)):
        arr.append(virusPos[i])
        setVirus(arr, i+1)
        arr.pop()


N, M = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(N)]

virusPos = []
for i in range(N):
    for j in range(N):
        if maze[i][j] == 2:
            virusPos.append([j, i])

setVirus([], 0)

min_v = math.inf
for res in results:
    if res != -1 and res < min_v:
        min_v = res

if min_v == math.inf:
    print(-1)
else:
    print(min_v)
