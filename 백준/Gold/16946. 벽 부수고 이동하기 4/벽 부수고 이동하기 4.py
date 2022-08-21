import sys
import random
from collections import deque
input = sys.stdin.readline

# 좌, 우, 상, 하
dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]


def BFS(x, y):
    Q = deque()
    Q.append([y, x])
    WALL_Q = deque()

    count = 1
    while Q:
        y, x = Q.popleft()
        for dir in range(4):
            ty = y + dy[dir]
            tx = x + dx[dir]

            if tx < 0 or ty < 0 or tx >= M or ty >= N:
                continue

            if not visited[ty][tx]:
                if board[ty][tx] == 1:
                    WALL_Q.append([ty, tx])
                    visited[ty][tx] = True
                    continue

                elif board[ty][tx] == 0:  # 방문처리 및 BFS
                    visited[ty][tx] = True
                    Q.append([ty, tx])
                    count += 1

    for y, x in WALL_Q:
        result_board[y][x] += count
        visited[y][x] = False


N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, list(input().rstrip())))

result_board = [[0] * M for _ in range(N)]


for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            result_board[i][j] = 1


visited = [[False] * M for i in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            BFS(j, i)


for i in range(N):
    for j in range(M):
        print(result_board[i][j] % 10, end='')
    print()
