from collections import deque
import sys

input = sys.stdin.readline


def BFS(x, y, graph, visited):
    # ↑ ↗ → ↘ ↓ ↙ ← ↖
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    Q = []
    Q.append([x, y])
    while Q:
        x, y = Q.pop()
        for i in range(8):
            ty = y + dy[i]
            tx = x + dx[i]

            if ty < 0 or tx < 0 or ty >= h or tx >= w:
                continue

            if graph[ty][tx] == 0:
                continue

            if not visited[ty][tx]:
                visited[ty][tx] = True
                Q.append([tx, ty])


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    arr = [[]*w for _ in range(h)]
    visited = [[False]*w for _ in range(h)]

    # 지도 입력
    for i in range(h):
        arr[i] = list(map(int, input().split()))

    count = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and arr[i][j] == 1:
                BFS(j, i, arr, visited)
                count += 1
    print(count)
