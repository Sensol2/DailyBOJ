X = int(input())
arr = [64]
count = 1
while X < sum(arr):
    left = min(arr) // 2
    right = min(arr) // 2

    arr[arr.index(min(arr))] = left
    if X <= sum(arr):
        continue
    else:
        arr.append(right)
    count += 1
print(count)
