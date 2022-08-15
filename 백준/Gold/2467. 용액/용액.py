import math

N = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)

left = 0
right = len(arr) - 1
result = [arr[left], arr[right]]
while left != right:
    solution = arr[left] + arr[right]
    if abs(solution) < abs(result[0] + result[1]):
        result = [arr[left], arr[right]]
    if solution < 0:
        left += 1
    elif solution > 0:
        right -= 1
    else:
        break
print(' '.join(map(str, result)))
