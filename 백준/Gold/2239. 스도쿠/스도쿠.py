from collections import deque
import sys


def GetAreaNumbers(y, x):  # 박스 내 숫자들
    px = x // 3
    py = y // 3
    arr = []
    for i in range(py*3, py*3 + 3):
        for j in range(px*3, px*3 + 3):
            if board[i][j] != 0:
                arr.append(board[i][j])
    return arr


def GetRowNumbers(y, x, exists):  # 가로
    arr = []
    for i in range(9):
        if board[y][i] != 0 and not board[y][i] in exists:
            arr.append(board[y][i])
    return arr


def GetColumnNumbers(y, x, exists):  # 세로
    arr = []
    for i in range(9):
        if board[i][x] != 0 and not board[i][x] in exists:
            arr.append(board[i][x])
    return arr


def Backtracking(y, x, Q, depth):
    candidate = list(range(1, 10))
    exists = []
    exists += GetAreaNumbers(y, x)
    exists += GetRowNumbers(y, x, exists)
    exists += GetColumnNumbers(y, x, exists)
    candidate = [x for x in candidate if x not in exists]

    for num in candidate:
        board[y][x] = num
        if len(Q) == depth:
            for i in range(9):
                for j in range(9):
                    print(board[i][j], end='')
                print()
            return -1
        ny, nx = Q[depth][0], Q[depth][1]
        res = Backtracking(ny, nx, Q, depth+1)
        if res == -1:
            return -1
        board[y][x] = 0


board = [[0]*9 for _ in range(9)]
Q = deque()
for i in range(9):
    board[i] = list(map(int, list(sys.stdin.readline().rstrip())))
    for j in range(9):
        if board[i][j] == 0:
            Q.append([i, j])


y, x = Q[0][0], Q[0][1]
Q.popleft()
Backtracking(y, x, Q, 0)
