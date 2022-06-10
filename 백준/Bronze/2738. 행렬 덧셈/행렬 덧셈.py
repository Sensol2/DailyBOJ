N, M = map(int, input().split())

arr = []

for i in range(N):
    arr += list(map(int, (input().split())))

arr2 = []
for i in range(N):
    arr2 += list(map(int, (input().split())))

count = 0
for i in range(N):
    for j in range(M):
        print(arr[count] + arr2[count], end=' ')
        count += 1
    print()
