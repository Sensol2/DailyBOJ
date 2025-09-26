import math

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

patternA = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
            ]

patternB = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
            ]

def count_repaint(x, y):
    # pattern A 체크
    countA = 0
    for i in range(8):
        for j in range(8):
            if board[y+i][x+j] != patternA[i][j]:
                countA += 1

    # pattern B 체크
    countB = 0
    for i in range(8):
        for j in range(8):
            if board[y+i][x+j] != patternB[i][j]:
                countB += 1

    return min(countA, countB)

ans = float('inf')

for i in range(N-7):
    for j in range(M-7):
        ans = min(ans, count_repaint(j, i))

print(ans)