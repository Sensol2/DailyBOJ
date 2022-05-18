import math
N = int(input())

arr = [[] * N for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))
    for j in range(N):
        if arr[i][j] == 0:
            arr[i][j] = math.inf

for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

for i in range(N):
    for j in range(N):
        if arr[i][j] == math.inf:
            print('0', end=' ')
        else:
            print('1', end=' ')
    print()
