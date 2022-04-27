from collections import deque

N, M = map(int, input().split())
maze = [[] * M for _ in range(N)]

# 상,하,좌,우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(N):
    maze[i] = list(input())

queue = deque()

cnt = 0
visited = [[False] * M for _ in range(N)] 

# 꼭짓점 제외하고, 탈출할 수 있는 칸 추가
for y in range(N):
    for x in range(M):
        if y == 0 and maze[y][x] == 'U': # 윗변
            queue.append((y,x))
            visited[y][x] = True
            cnt += 1
        if y == N-1 and maze[y][x] == 'D': # 아랫변
            queue.append((y,x))
            visited[y][x] = True
            cnt += 1
        if x == 0 and maze[y][x] == 'L': # 왼변
            queue.append((y,x))
            visited[y][x] = True
            cnt += 1
        if x == M-1 and maze[y][x] == 'R': # 오른변
            queue.append((y,x))
            visited[y][x] = True
            cnt += 1

while queue:
    item = queue.popleft()
    y, x = item[0], item[1]

    for i in range(4): # 상,하,좌,우
        tx = x + dx[i]
        ty = y + dy[i]

        if tx < 0 or tx >= M or ty < 0 or ty >= N: #맵 이탈
            continue
        
        if not visited[ty][tx]:
            if i == 0 and maze[ty][tx] == 'D': # 윗쪽 칸이 D인 경우
                visited[ty][tx] = True
                queue.append((ty, tx))
                cnt += 1
            if i == 1 and maze[ty][tx] == 'U': # 아랫쪽 칸이 U인 경우
                visited[ty][tx] = True
                queue.append((ty, tx))
                cnt += 1
            if i == 2 and maze[ty][tx] == 'R': # 왼쪽 칸이 R인 경우
                visited[ty][tx] = True
                queue.append((ty, tx))
                cnt += 1
            if i == 3 and maze[ty][tx] == 'L': # 오른쪽 칸이 L인 경우
                visited[ty][tx] = True
                queue.append((ty, tx))
                cnt += 1
print(cnt)
