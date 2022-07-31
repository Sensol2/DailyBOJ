from collections import deque
from re import U

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def Flood(fQ, bQ, f_visited, b_visited):
    FQ = deque(fQ)
    BQ = deque(bQ)

    level = 0
    while True:
        # 홍수 일으키기
        while FQ:
            if level < FQ[0][2]:
                break
            x, y, depth = FQ.popleft()

            for i in range(4):
                ty = y + dy[i]
                tx = x + dx[i]

                if tx < 0 or ty < 0 or tx >= C or ty >= R:
                    continue

                if board[ty][tx] == 'D':
                    continue

                if board[ty][tx] == 'X':
                    continue

                if not f_visited[ty][tx]:
                    f_visited[ty][tx] = True
                    board[ty][tx] = '*'
                    FQ.append([tx, ty, depth+1])
        # 비버 이동하기
        while BQ:
            if level < BQ[0][2]:
                break
            x, y, depth = BQ.popleft()

            for i in range(4):
                ty = y + dy[i]
                tx = x + dx[i]

                if tx < 0 or ty < 0 or tx >= C or ty >= R:
                    continue

                if board[ty][tx] == '*':
                    continue

                if board[ty][tx] == 'X':
                    continue

                if board[ty][tx] == 'D':
                    return depth + 1

                if not b_visited[ty][tx]:
                    b_visited[ty][tx] = True
                    board[ty][tx] = 'S'
                    BQ.append([tx, ty, depth+1])
        if not BQ:
            return "KAKTUS"
        level += 1


R, C = map(int, input().split())
board = [['']*C for _ in range(R)]

# 홍수 시작 포지션
FQ = []
# 비버 시작 포지션
BQ = []

f_visited = [[False]*C for _ in range(R)]
b_visited = [[False]*C for _ in range(R)]

for i in range(R):
    board[i] = list(input())
    for j in range(C):
        if board[i][j] == '*':
            FQ.append([j, i, 0])
            f_visited[i][j] = True
        if board[i][j] == 'S':
            BQ.append([j, i, 0])
            b_visited[i][j] = True


print(Flood(FQ, BQ, f_visited, b_visited))
