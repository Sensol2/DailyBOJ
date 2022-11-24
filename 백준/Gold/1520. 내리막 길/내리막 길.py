# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(x, y):
    if x == N-1 and y == M-1:
        return 1

    if DP[y][x] != -1:
        return DP[y][x]

    DP[y][x] = 0
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]

        if tx < 0 or ty < 0 or tx >= N or ty >= M:
            continue

        if arr[y][x] > arr[ty][tx]:  # 내리막길인 경우만
            DP[y][x] += dfs(tx, ty)

    return DP[y][x]


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
DP = [[-1] * (N) for _ in range(M)]
dfs(0, 0)
print(DP[0][0])
