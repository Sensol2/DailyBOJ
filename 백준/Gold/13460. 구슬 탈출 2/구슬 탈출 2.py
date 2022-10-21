from collections import deque
import sys
input = sys.stdin.readline

errnum = 0
# 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def move(i, _x, _y):
    cnt = 0
    x, y = _x, _y
    while True:
        ty = y + dy[i]
        tx = x + dx[i]

        if maze[ty][tx] == '#':
            return [x, y, cnt]
        if maze[ty][tx] == 'O':
            return [tx, ty, cnt]
        else:
            x = tx
            y = ty
            cnt += 1


def bfs(rx, ry, bx, by, depth):
    Q = deque()
    Q.append([rx, ry, bx, by, depth])
    visited = [[[[False]*M for _ in range(N)]
                for _ in range(M)] for _ in range(N)]
    while Q:
        rx, ry, bx, by, depth = Q.popleft()
        if depth > 10:
            break
        for i in range(4):
            nrx, nry, count_r = move(i, rx, ry)
            nbx, nby, count_b = move(i, bx, by)

            if maze[nby][nbx] == 'O':
                continue

            if maze[nry][nrx] == 'O':
                return depth

            if nrx == nbx and nry == nby:  # 겹쳤을 때
                if count_r > count_b:  # 빨간공이 더 갔으면
                    nrx -= dx[i]
                    nry -= dy[i]
                else:  # 파란공이 더 갔으면
                    nbx -= dx[i]
                    nby -= dy[i]

            if not visited[nry][nrx][nby][nbx]:
                visited[nry][nrx][nby][nbx] = True
                Q.append([nrx, nry, nbx, nby, depth+1])
    return -1


N, M = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if maze[i][j] == 'R':
            rx = j
            ry = i
        if maze[i][j] == 'B':
            bx = j
            by = i

print(bfs(rx, ry, bx, by, 1))
