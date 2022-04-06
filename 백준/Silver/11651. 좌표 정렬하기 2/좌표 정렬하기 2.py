N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

result = sorted(arr, key=lambda x: (x[1], x[0]))
for i in result:   
    print(i[0], i[1])