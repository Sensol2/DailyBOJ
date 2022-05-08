from collections import *
import copy
import sys

def BFS(maze, _x, _y):
    maze_origin = copy.deepcopy(maze)
    # 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    visited = [[False] * M for _ in range(N)]
    alreadyBreak = [[False] * M for _ in range(N)]

    # 첫 위치 Init
    queue = deque()
    queue.append([_y, _x])
    maze[_y][_x] = 1
    
    while queue:
        item = queue.popleft()
        y, x = item[0], item[1]

        if y == N-1 and x == M-1: # 목적지 도착
            return maze[y][x]

        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]

            if ty < 0 or ty >= N or tx < 0 or tx >= M:
                continue
            
            breaked = False
            if maze[ty][tx] == 1:
                if not alreadyBreak[y][x]:
                    maze[ty][tx] = 0
                    alreadyBreak[ty][tx] = True
                    breaked = True


            if not alreadyBreak[y][x] and alreadyBreak[ty][tx] and not breaked and maze_origin[ty][tx] != 1:
                alreadyBreak[ty][tx] = False
                visited[ty][tx] = False

            if maze[ty][tx] != 1 and not visited[ty][tx]:
                visited[ty][tx] = True
                queue.append([ty, tx])
                maze[ty][tx] = maze[y][x] + 1

                if alreadyBreak[y][x]:
                    alreadyBreak[ty][tx] = True



    return -1

N, M = map(int, input().split())
maze = [[] * M for _ in range(N)]

wall_pos = []
for i in range(N):
    maze[i] = list(map(int, list(sys.stdin.readline().strip())))

results = []
results.append(BFS(maze, 0, 0))

if max(results) != -1:
    results = [i for i in results if i not in [-1]]
    print(min(results))
else:
    print(-1)
    