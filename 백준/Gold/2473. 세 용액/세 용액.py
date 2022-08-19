import math


N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

result = [math.inf]
for i in range(N-2):
    j = i+1
    k = N-1
    while j != k:
        if abs(arr[i]+arr[j]+arr[k]) < abs(sum(result)):
            result = [arr[i], arr[j], arr[k]]
        if arr[i] + arr[j] + arr[k] < 0:
            j += 1
        elif arr[i] + arr[j] + arr[k] > 0:
            k -= 1
        elif arr[i] + arr[j] + arr[k] == 0:
            break

print(' '.join(map(str, sorted(result))))
