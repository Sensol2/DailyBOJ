from collections import deque


def show_arr(cx, cy):  # for debugging
    print()
    for i in range(N):
        for j in range(N):
            if i == cy and j == cx:
                print("■", end=' ')
            else:
                print(arr[i][j], end=' ')
        print()


def find_fish(sx, sy, size):
    # 상, 좌, 하, 우
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    Q = deque()
    Q.append([sx, sy, 0])
    visisted = [[False]*N for _ in range(N)]
    visisted[sy][sx] = True

    eatable_fish_pos = []
    while Q:
        x, y, depth = Q.popleft()

        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]

            if tx < 0 or ty < 0 or tx >= N or ty >= N:
                continue

            if arr[ty][tx] > size:
                continue

            if not visisted[ty][tx]:
                if arr[ty][tx] != 0 and arr[ty][tx] < size:
                    eatable_fish_pos.append([tx, ty, depth+1])
                visisted[ty][tx] = True
                Q.append([tx, ty, depth+1])

    if not eatable_fish_pos:
        return -1

    next_fish_pos = sorted(eatable_fish_pos, key=lambda x: (x[2], x[1], x[0]))
    return next_fish_pos[0]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

sx = 0
sy = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:  # 아기상어의 위치
            sx = j
            sy = i
            arr[i][j] = 0

count = 0
size = 2
exp = 0
while True:
    r = find_fish(sx, sy, size)
    if r == -1:
        print(count)
        break

    # 물고기 위치 재배치
    sx = r[0]
    sy = r[1]
    count += r[2]

    # 물고기 먹었을 때의 처리
    arr[sy][sx] = 0
    exp += 1
    if exp == size:
        size += 1
        exp = 0

    # show_arr(sx, sy)
