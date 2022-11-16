from collections import deque


def bfs(x, y):
    # 상, 하, 좌, 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    Q = deque()
    Q.append([x, y, 1])
    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True
    max_distance = 0
    while Q:
        x, y, depth = Q.popleft()
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]

            if tx < 0 or ty < 0 or tx >= M or ty >= N:
                continue

            if arr[ty][tx] == 'W':
                continue

            if not visited[ty][tx]:
                visited[ty][tx] = True
                Q.append([tx, ty, depth+1])
                if max_distance < depth+1:
                    max_distance = depth
    return max_distance


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

results = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':  # 육지라면
            res = bfs(j, i)
            results.append(res)

print(max(results))
