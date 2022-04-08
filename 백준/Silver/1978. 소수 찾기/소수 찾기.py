import itertools
from collections import deque

arr = [False, False] + [True] * 9999
for i in range(2, 101):
    if arr[i]:
        for j in range(i*2, len(arr), i):
            arr[j] = False

N = int(input())
nums = list(map(int, input().split()))

sum_value = 0
for num in nums:
    if arr[num]:
        sum_value += 1
print(sum_value)