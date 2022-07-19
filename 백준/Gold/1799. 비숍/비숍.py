import copy
from random import randint

results = []


def ExceptColor(arr, color):
    for i in range(N):
        for j in range(N):
            if color == "white":
                if (i+j) % 2 == 0:
                    arr[i][j] = 0
            if color == "black":
                if (i+j) % 2 != 0:
                    arr[i][j] = 0


def CheckCollision(x, y, bishops):  # (x,y)에 비숍을 놓을 때 충돌 확인
    for bishop in bishops:
        dy, dx = bishop[0], bishop[1]
        if abs(dy-y) == abs(dx-x):
            return True
    return False


def Backtracking(x, y, board, bishops):
    if x == N and y == N-1:  # 체스판 끝에 다다르면
        global results
        results.append(len(bishops))
        return

    if x == N:  # 다음 행 이동
        Backtracking(0, y+1, board, bishops)
        return

    # 비숍을 놓을 수 있으면
    if board[y][x] == 1 and not CheckCollision(x, y, bishops):
        # 비숍을 놓거나
        board[y][x] = 2
        bishops.append((y, x))
        Backtracking(x+1, y, board, bishops)
        board[y][x] = 1
        bishops.pop()
        # 비숍을 놓지 않기
        Backtracking(x+1, y, board, bishops)
    else:
        Backtracking(x+1, y, board, bishops)


N = int(input())
board = [[0]*N for _ in range(N)]
white_board = None
black_board = None
for i in range(N):
    board[i] = list(map(int, input().split()))

white_board = copy.deepcopy(board)
black_board = copy.deepcopy(board)
ExceptColor(white_board, "black")
ExceptColor(black_board, "white")

bishops = []
white_count = 0
black_count = 0

Backtracking(0, 0, white_board, bishops)
white_count = max(results)
results = []
Backtracking(0, 0, black_board, bishops)
black_count = max(results)
print(white_count + black_count)
