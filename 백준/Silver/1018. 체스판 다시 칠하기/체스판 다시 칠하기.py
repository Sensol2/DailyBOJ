def RepaintArea(board, y, x):
    count = 0
    if board[y][x] == 'W': # 첫번째 칸이 W인 경우
        for i in range(8):
            if i % 2 == 0:
                pattern = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
            else:
                pattern = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

            for j in range(8):
                if board[y+i][x+j] != pattern[j]:
                    count += 1

    if board[y][x] == 'B': # 첫번째 칸이 B인 경우
        for i in range(8):
            if i % 2 == 0:
                pattern = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
            else:
                pattern = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']

            for j in range(8):
                if board[y+i][x+j] != pattern[j]:
                    count += 1

    return count

N, M = map(int, input().split())
board = [[] for _ in range(N)]
for i in range(N):
    board[i] = list(input())

results = []
for i in range(0, (N-8)+1):
    for j in range(0, (M-8)+1):
        results.append(RepaintArea(board, i, j))
        board2 = list(board)
        if board2[i][j] == 'W':
            board2[i][j] = 'B'
        else:
            board2[i][j] = 'W'
        results.append(RepaintArea(board2, i, j) + 1)

print(min(results))