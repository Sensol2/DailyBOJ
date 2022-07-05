from collections import deque
import sys
import time


def GetAreaNumbers(y, x):  # 박스 내 숫자들
    px = x // 3
    py = y // 3
    arr = []
    for i in range(py*3, py*3 + 3):
        for j in range(px*3, px*3 + 3):
            if board[i][j] != 0:
                arr.append(board[i][j])
    return arr


def GetRowNumbers(y, x):  # 가로
    arr = []
    for i in range(9):
        if board[y][i] != 0:
            arr.append(board[y][i])
    return arr


def GetColumnNumbers(y, x):  # 세로
    arr = []
    for i in range(9):
        if board[i][x] != 0:
            arr.append(board[i][x])
    return arr


count = 0


def Backtracking(y, x, Q, depth):
    global count
    count += 1
    candidate = list(range(1, 10))
    exists = []
    exists += GetAreaNumbers(y, x)
    exists += GetRowNumbers(y, x)
    exists += GetColumnNumbers(y, x)

    # candidate - exists (차집합)
    candidate = [x for x in candidate if x not in exists]

    for num in candidate:
        board[y][x] = num
        if len(Q) == depth:
            for i in range(9):
                for j in range(9):
                    print(board[i][j], end=' ')
                print()
            return -1
        ny, nx = Q[depth][0], Q[depth][1]
        res = Backtracking(ny, nx, Q, depth+1)
        if res == -1:  # -1 반환시 즉시 백트래킹 탈출, 종료
            return -1
        board[y][x] = 0


board = [[0]*9 for _ in range(9)]
Q = deque()  # 비어 있는 칸들의 좌표 큐
for i in range(9):
    board[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(9):
        if board[i][j] == 0:
            Q.append([i, j])


# 백트래킹 시작위치 초기화
y, x = Q[0][0], Q[0][1]
Q.popleft()
Backtracking(y, x, Q, 0)
