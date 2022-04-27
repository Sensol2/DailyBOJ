from collections import deque

N, M = map(int, input().split())
maze = [[] * M for _ in range(N)]

# 상,좌,하,우
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

for i in range(N):
    maze[i] = list(input())

queue = deque()

cnt = 0
visited = [[False] * M for _ in range(N)] 

# 탈출할 수 있는 칸 추가
for y in range(N):
    for x in range(M):
        if (y == 0 and maze[y][x] == 'U') or (y == N-1 and maze[y][x] == 'D') or (x == 0 and maze[y][x] == 'L') or (x == M-1 and maze[y][x] == 'R'):
            queue.append((y,x))
            visited[y][x] = True
            cnt += 1

direction_list = ['U', 'L', 'D', 'R']
while queue:
    item = queue.popleft()
    y, x = item[0], item[1]

    for i in range(4): # 상,좌,하,우
        tx = x + dx[i]
        ty = y + dy[i]

        if tx < 0 or tx >= M or ty < 0 or ty >= N: #맵 이탈
            continue
        
        if not visited[ty][tx]:
            if maze[ty][tx] == direction_list[(i+2)%4]:
                visited[ty][tx] = True
                queue.append((ty, tx))
                cnt += 1
print(cnt)