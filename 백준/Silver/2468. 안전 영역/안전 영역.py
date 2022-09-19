from collections import deque
import sys

input = sys.stdin.readline


def BFS(x, y, visited, level):
    # 동, 서, 남, 북
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    count = 0
    Q = deque()
    Q.append([x, y])
    visited[y][x] = True
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]

            if tx < 0 or ty < 0 or tx >= N or ty >= N:
                continue

            if arr[ty][tx] <= level:
                continue

            if not visited[ty][tx]:
                visited[ty][tx] = True
                Q.append([tx, ty])


N = int(input())
arr = [[] * N for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

results = []
# 높이 1부터 100까지 물이 차오름
for level in range(101):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for col in range(N):
        for row in range(N):
            if arr[col][row] <= level:  # 위험지대
                visited[col][row] = True
                continue
            if not visited[col][row]:
                BFS(row, col, visited, level)
                cnt += 1
    results.append(cnt)
print(max(results))
