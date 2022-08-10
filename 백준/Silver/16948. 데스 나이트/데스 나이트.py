from collections import deque


def BFS(x, y):
    dx = [-2, -2, 0, 0, 2, 2]
    dy = [-1, 1, -2, 2, -1, 1]
    Q = deque()
    Q.append([x, y, 1])
    board[y][x] = 1
    visisted = [[False] * N for _ in range(N)]
    visisted[y][x] = True

    while Q:
        x, y, depth = Q.popleft()
        for i in range(6):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or ty < 0 or tx >= N or ty >= N:
                continue

            if tx == r2 and ty == c2:
                return depth

            if not visisted[ty][tx]:
                Q.append([tx, ty, depth+1])
                visisted[ty][tx] = True
                board[ty][tx] = 1
    return -1


N = int(input())
board = [[0]*N for _ in range(N)]
r1, c1, r2, c2 = map(int, input().split())
print(BFS(r1, c1))
