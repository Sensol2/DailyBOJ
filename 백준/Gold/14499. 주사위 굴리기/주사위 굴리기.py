N, M, y, x, K = map(int, input().split())

arr = [[] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

diceX = [0,0,0,0]
diceY = [0,0,0,0]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
commands = list(map(int, input().split()))

for command in commands:
    tx = x + dx[command-1]
    ty = y + dy[command-1]

    if tx < 0 or tx >= M or ty < 0 or ty >= N:
        continue
    else:
        x = tx
        y = ty

        if command == 1: #동쪽
            back = diceY[3]
            diceY = diceY[0:3]
            diceY.insert(0, back)
            diceX[1] = diceY[1]
            diceX[3] = diceY[3]
        
        if command == 2: #서쪽
            front = diceY[0]
            diceY = diceY[1:4]
            diceY.append(front)
            diceX[1] = diceY[1]
            diceX[3] = diceY[3]

        if command == 3: #북쪽
            front = diceX[0]
            diceX = diceX[1:4]
            diceX.append(front)
            diceY[1] = diceX[1]
            diceY[3] = diceX[3]

        if command == 4: #남쪽
            back = diceX[3]
            diceX = diceX[0:3]
            diceX.insert(0, back)
            diceY[1] = diceX[1]
            diceY[3] = diceX[3]

        if arr[y][x] == 0:
            arr[y][x] = diceX[3]
        else:
            diceX[3] = arr[y][x]
            diceY[3] = arr[y][x]
            arr[y][x] = 0

        print(diceX[1])