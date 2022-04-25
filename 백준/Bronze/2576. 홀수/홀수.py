arr = []
for i in range(7):
    N = int(input())
    if N % 2 != 0:
        arr.append(N)
if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)