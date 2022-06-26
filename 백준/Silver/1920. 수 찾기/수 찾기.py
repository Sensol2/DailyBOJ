numdict = dict()


N = int(input())
numset = list(map(int, input().split()))

for i in numset:
    numdict[i] = True


M = int(input())
arr = list(map(int, input().split()))

for i in arr:
    if i in numdict.keys():
        print(1)
    else:
        print(0)
