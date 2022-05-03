from itertools import *

N, M = map(int, input().split())
arr = list(range(1, N+1))

for i in list(combinations(arr, M)):
    for j in i:
        print(j, end=' ')
    print()