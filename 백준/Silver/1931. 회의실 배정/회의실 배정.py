M = int(input())
arr = []

for i in range(M):
    a, b = map(int, input().split())
    arr.append((a, b))

arr = sorted(arr, key=lambda x: (x[1], x[0]))

res = []
recent_end = 0
for i in arr:
    start, end = i[0], i[1]
    if recent_end <= start:
        res.append(i)
        recent_end = i[1]

print(len(res))
