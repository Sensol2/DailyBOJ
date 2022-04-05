from collections import deque
import sys, time

# 디버깅용
def ShowBox(box):
    print("=========================")
    for i in range(N):
        for j in range(M):
            print(box[i][j], end=" ")
        print()

# 순서대로 BFS로 박스 업데이트
def SimulateRipe(box, _ripe):
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
            y, x = currItem[0], currItem[1]

            for i in range(4):
                ty = y + dy[i]
                tx = x + dx[i]
                if ty < 0 or ty >= N or tx < 0 or tx >= M:
                    continue
                if box[ty][tx] == 0:
                    flag = True
                    ripedCount += 1
                    box[ty][tx] = 1
                    new_ripe.append((ty, tx))

        if flag:
            count += 1
        # ShowBox(box)
    return count, ripedCount

# 입력부
M, N= map(int, sys.stdin.readline().split())

box = [[0]*M for _ in range(N)]

ripe = []
unripeCount = 0
for i in range(N):
    box[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if box[i][j] == 1:
            ripe.append((i, j))
        if box[i][j] == 0:
            unripeCount += 1

result, ripedCount = SimulateRipe(box, ripe)

if unripeCount - ripedCount > 0:
    print("-1")
else:
    print(result)