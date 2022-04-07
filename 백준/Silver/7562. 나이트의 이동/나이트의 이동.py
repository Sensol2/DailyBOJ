from collections import deque

def BFS(board, _y, _x, visited):
    if board[_y][_x] == -1: # 이미 도착지점이면 0 리턴
        return 0

    count = 1
    # 나이트 이동의 모든 경우의 수
    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    dx = [1, 2, 2, 1, -1, -2, -2, -1]

    queue = deque()
    queue.append([_y, _x])
    new_queue = deque()
    while True:
        if new_queue:
            queue = new_queue
            new_queue = deque()
        while queue:
            y, x = queue.popleft()

            for i in range(8):
                ty = y + dy[i]
                tx = x + dx[i]

                if tx < 0 or tx >= I or ty < 0 or ty >= I:
                    continue
                if not visited[ty][tx]:

                    if board[ty][tx] == -1:
                        return count
                    else:
                        board[ty][tx] = count
                        visited[ty][tx] = True
                        new_queue.append([ty, tx])
        count += 1


N = int(input())
for i in range(N):
    I = int(input())
    board = [[0] * I for _ in range(I)]
    visited = [[False] * I for _ in range(I)]

    x, y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    board[goal_y][goal_x] = -1   # 도착지점 -1로 표시

    cnt = BFS(board, y, x, visited)
    print(cnt)