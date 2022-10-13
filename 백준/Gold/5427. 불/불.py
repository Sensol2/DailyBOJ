from collections import deque
import sys

input = sys.stdin.readline


def SpreadFire(Q, f_visited):
    # 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    return_Q = deque()
    while Q:
        x, y = Q.popleft()
        f_visited[y][x] = True
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if ty < 0 or tx < 0 or tx >= w or ty >= h:
                continue

            if maze[ty][tx] == '#':
                continue

            if not f_visited[ty][tx]:
                maze[ty][tx] = '*'
                f_visited[ty][tx] = True
                return_Q.append([tx, ty])
    return return_Q


def Movewharacter(player_x, player_y, Fire_Q):
    # 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visited = [[False]*w for i in range(h)]
    f_visited = [[False]*w for i in range(h)]

    Q = deque()
    Q.append([player_x, player_y, 0])
    next_Q = deque()

    visited[player_y][player_x] = True
    flag = True
    while flag:
        if next_Q:
            Q = next_Q
            next_Q = deque()
        flag = False
        while Q:
            x, y, cnt = Q.popleft()
            if maze[y][x] == '*':
                continue
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]

                if ty < 0 or tx < 0 or tx >= w or ty >= h:
                    print(cnt+1)
                    return

                if maze[ty][tx] == '#' or maze[ty][tx] == '*':
                    continue

                if not visited[ty][tx]:
                    flag = True
                    maze[ty][tx] = '@'
                    visited[ty][tx] = True
                    next_Q.append([tx, ty, cnt+1])
        Fire_Q = SpreadFire(Fire_Q, f_visited)
    print("IMPOSSIBLE")
    return


T = int(input())
for t in range(T):
    w, h = map(int, input().split())
    maze = [[None]*w for i in range(h)]

    Fire_Q = deque()

    playerPos_x = 0
    playerPos_y = 0
    for i in range(h):
        maze[i] = list(input())
        for j in range(w):
            if maze[i][j] == '*':
                Fire_Q.append([j, i])
            if maze[i][j] == '@':
                playerPos_y = i
                playerPos_x = j
    Movewharacter(playerPos_x, playerPos_y, Fire_Q)
