N, M = map(int, input().split())

shape = [[0]*M for _ in range(N)]

for i in range(N):
    shape[i] = list(input())

for i in range(N):
    for j in range(M-1, -1, -1):
        print(shape[i][j], end='')
    print()
