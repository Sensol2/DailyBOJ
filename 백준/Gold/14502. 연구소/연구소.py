from collections import deque

# 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def BFS(area, virus_pos, visited):
    infected_area = 0

    queue = deque()
    for virus in virus_pos:
        y, x = virus[0], virus[1]
        visited[y][x] = True
        queue.append([y, x])

    while queue:
        item = queue.popleft()
        y, x = item[0], item[1]
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]

            if ty < 0 or ty >= N or tx < 0 or tx >= M:
                continue
            if area[ty][tx] == 0 and not visited[ty][tx]:
                visited[ty][tx] = True
                queue.append([ty, tx])
                infected_area += 1
    
    return infected_area


N, M = map(int, input().split())

area = [[0] * M for _ in range(N)]

safe_area = 0   # 안전지대 개수
safearea_pos = []
virus_pos = []
for i in range(N):
    area[i] = list(map(int, input().split()))
    for j in range(M):
        if area[i][j] == 0:
            safe_area += 1
        if area[i][j] == 0:
            safearea_pos.append([i, j])
        if area[i][j] == 2:
            virus_pos.append([i, j])

safe_area -= 3 # 벽 3개 세우면 그만큼 안전지대 줄어드니까

best = []
for i in safearea_pos:
    for j in safearea_pos[1:]:
        for k in safearea_pos[2:]:
            # 벽 3개 브루트포스로 세우기
            area[i[0]][i[1]] = 1
            area[j[0]][j[1]] = 1
            area[k[0]][k[1]] = 1
            
            visited = [[False] * M for _ in range(N)]
            infected_area = BFS(area, virus_pos, visited)
            best.append(safe_area-infected_area)
            #벽 초기화
            area[i[0]][i[1]] = 0
            area[j[0]][j[1]] = 0
            area[k[0]][k[1]] = 0

print(max(best))