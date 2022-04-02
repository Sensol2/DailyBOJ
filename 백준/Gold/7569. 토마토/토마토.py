from collections import deque
import sys, time

# 디버깅용
def ShowBox(box):
    print("=========================")
    for h in range(H):
        for i in range(N):
            for j in range(M):
                print(box[h][i][j], end=" ")
            print()

# 순서대로 BFS로 박스 업데이트
def SimulateRipe(box, _ripe):
    # 상하층
    dh = [-1, 1]
    # 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    count = 0
    # new_ripe: 새롭게 익은 토마토들의 큐
    ripe = deque(_ripe)
    new_ripe = deque()

    ripedCount = 0
    # flag: 하나라도 익으면 True로 갱신, 아무 변화도 없으면 False가 되어 루프 탈출
    flag = True
    while flag:
        if new_ripe:
            ripe = new_ripe
            new_ripe = deque()
        flag = False
        while ripe:
            currItem = ripe.popleft()
            h, y, x = currItem[0], currItem[1], currItem[2]
            # 한 층에 대해서 상하좌우 계산
            for i in range(4):
                ty = y + dy[i]
                tx = x + dx[i]
                if ty < 0 or ty >= N or tx < 0 or tx >= M:
                    continue
                if box[h][ty][tx] == 0:
                    flag = True
                    ripedCount += 1
                    box[h][ty][tx] = 1
                    new_ripe.append((h, ty, tx))

            # 인접 상, 하층에 대해 계산
            for i in range(2):
                th = h + dh[i]

                if th < 0 or th >= H:
                    continue
                if box[th][y][x] == 0:
                    flag = True
                    ripedCount += 1
                    box[th][y][x] = 1
                    new_ripe.append((th, y, x))
        if flag:
            count += 1
        # ShowBox(box)
    return count, ripedCount

# 입력부
M, N, H = map(int, sys.stdin.readline().split())

box = [[[0]*M for _ in range(N)] for _ in range(H)]

ripe = []
unripeCount = 0
for h in range(H):
    for i in range(N):
        box[h][i] = list(map(int, sys.stdin.readline().split()))
        for j in range(M):
            if box[h][i][j] == 1:
                ripe.append((h, i, j))
            if box[h][i][j] == 0:
                unripeCount += 1

result, ripedCount = SimulateRipe(box, ripe)

if unripeCount - ripedCount > 0:
    print("-1")
else:
    print(result)
