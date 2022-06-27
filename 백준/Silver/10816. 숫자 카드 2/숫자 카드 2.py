N = int(input())
numset = list(map(int, input().split()))
numdict = dict()
for num in numset:
    if num in numdict.keys():
        numdict[num] += 1
    else:
        numdict[num] = 1

M = int(input())
nums = list(map(int, input().split()))
for num in nums:
    if num in numdict.keys():
        print(numdict[num], end=' ')
    else:
        print(0, end=' ')
