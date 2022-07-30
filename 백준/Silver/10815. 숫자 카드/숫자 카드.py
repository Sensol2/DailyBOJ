N = int(input())
lst1 = map(int, input().split())
numset = dict()
for i in lst1:
    numset[i] = 1
M = int(input())
lst2 = map(int, input().split())
for i in lst2:
    if i in numset.keys():
        print(1, end=' ')
    else:
        print(0, end=' ')
