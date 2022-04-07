import itertools
from collections import deque

# 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def BFS(area, virus_pos, visited):
    time_count = 0
    infectedCoount = 0

    queue = deque()
    for virus in virus_pos:
        y, x = virus[0], virus[1]
        visited[y][x] = True
        queue.append([y, x])

    new_queue = deque()
    flag = True
    while flag:
        flag = False
        if new_queue:
            queue = new_queue
            new_queue = deque()
        while queue:
            item = queue.popleft()
            y, x = item[0], item[1]
            for i in range(4):
                ty = y + dy[i]
                tx = x + dx[i]

                if ty < 0 or ty >= N or tx < 0 or tx >= N:
                    continue
                if area[ty][tx] == 0 and not visited[ty][tx]:
                    visited[ty][tx] = True
                    new_queue.append([ty, tx])
                    flag = True
                    infectedCoount += 1
        time_count -= 1
    time_count += 1
    return abs(time_count), infectedCoount

N, M = map(int, input().split())

area = [[0] * M for _ in range(N)]


safearea_cnt = 0   # 안전지대 개수
virusarea_cnt = 0   # 바이러스 지대 개수
safearea_pos = []
virus_pos = []
for i in range(N):
    area[i] = list(map(int, input().split()))
    for j in range(N):
        if area[i][j] == 0:
            safearea_cnt += 1
        if area[i][j] == 0:
            safearea_pos.append([i, j])
        if area[i][j] == 2:
            virus_pos.append([i, j])
            virusarea_cnt += 1

# # 바이러스를 M만큼 배치하고 남은 지역은 Safearea가 되므로.
safearea_cnt += virusarea_cnt - M


min_case = []
# 바이러스 위치 경우의 수 브루트포스로 전부 검사
for case in list(itertools.combinations(virus_pos, M)):
    # 바이러스 위치 전부 0으로 초기화
    for v in virus_pos:
        area[v[0]][v[1]] = 0

    for virus in case:
        area[virus[0]][virus[1]] = 2

    visited = [[False] * N for _ in range(N)]
    cnt, infectedCount = BFS(list(area), case, visited)
    if safearea_cnt - infectedCount > 0:
        continue
    else:
        min_case.append(cnt)

if min_case:
    print(min(min_case))
else:
    print(-1)