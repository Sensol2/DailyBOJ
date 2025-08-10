N = int(input())

board = [list(input()) for _ in range(N)]
solution = [[0]*N for _ in range(N)]

# 8방향
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
for y in range(N):
    for x in range(N):
        if board[y][x] == '.': # 빈 칸인 경우
            for k in range(8):
                tx = x + dx[k]
                ty = y + dy[k]

                if 0 <= tx and 0 <= ty and tx < N and ty < N:
                    if board[ty][tx] != '.':
                        solution[y][x] += int(board[ty][tx])
                        if solution[y][x] >= 10:
                            solution[y][x] = 'M'
                            break
        else:
            solution[y][x] = "*"

for y in range(N):
    for x in range(N):
        print(solution[y][x], end='')
    print()