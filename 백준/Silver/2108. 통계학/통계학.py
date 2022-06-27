import sys
import math
from collections import Counter


def findmodes(arr):
    c = Counter(arr)
    common = c.most_common()
    result = []
    for i in common:
        if i[1] == common[0][1]:
            result.append(i[0])
    return sorted(result)


input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))

arr = sorted(arr)
print(round(sum(arr)/N))
print(arr[len(arr)//2])

res = findmodes(arr)
if len(res) >= 2:
    print(res[1])
else:
    print(res[0])
print(abs(max(arr)-min(arr)))
