from collections import deque

N = int(input())
arr = list(range(1, N+1))
arr = deque(arr)

while len(arr) > 1:
    arr.popleft()
    arr.append(arr[0])
    arr.popleft()

print(arr[0])