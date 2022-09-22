from collections import deque


def BFS(x, y, visited):
    # 상, 하, 좌, 우
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    Q = deque()
    Q.append([x, y])

    visited[y][x] = True
    count = 1
    while Q:
        x, y = Q.pop()
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]

            if tx < 0 or ty < 0 or tx >= M or ty >= N:
                continue

            if arr[ty][tx] == 0:
                continue

            if not visited[ty][tx]:
                visited[ty][tx] = True
                Q.append([tx, ty])
                count += 1
    return count


N, M = map(int, input().split())
arr = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

results = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            if not visited[i][j]:
                res = BFS(j, i, visited)
                results.append(res)

if results:
    print(len(results))
    print(max(results))
else:
    print("0")
    print("0")
