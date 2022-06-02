import sys

input = sys.stdin.readline

mydict = dict()
N = int(input())

for i in range(N):
    num = int(input())
    if num in mydict:
        mydict[num] += 1
    else:
        mydict[num] = 1

for i in sorted(mydict):
    for j in range(mydict[i]):
        print(i)
