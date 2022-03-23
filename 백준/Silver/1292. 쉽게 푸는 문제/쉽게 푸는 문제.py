A, B = map(int, input().split())
arr = []

for i in range(1000):
    for j in range(i):
        arr.append(i)
sum = 0
for i in range(A-1, B, 1):
    sum += arr[i]
print(sum)