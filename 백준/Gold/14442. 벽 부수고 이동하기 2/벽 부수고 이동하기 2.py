import sys
from collections import deque

input = sys.stdin.readline

# 좌, 우, 하, 상
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def BFS(x, y, K):
    visited = [[[-1] * M for _ in range(N)] for _ in range(K+1)]
    Q = deque()
    Q.append([0, 0, 0])

    visited[0][0][0] = 0
    while Q:
        y, x, k = Q.popleft()
        if x == M-1 and y == N-1:  # 도착
            return visited[k][y][x]+1

        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if 0 <= tx < M and 0 <= ty < N:
                if board[ty][tx] == 1 and k < K and visited[k+1][ty][tx] == -1:  # 벽 부수기
                    Q.append([ty, tx, k+1])
                    visited[k+1][ty][tx] = visited[k][y][x]+1

                elif board[ty][tx] == 0 and visited[k][ty][tx] == -1:  # 방문처리 및 BFS
                    Q.append([ty, tx, k])
                    visited[k][ty][tx] = visited[k][y][x]+1
    return -1


N, M, K = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]
print(BFS(0, 0, K))
