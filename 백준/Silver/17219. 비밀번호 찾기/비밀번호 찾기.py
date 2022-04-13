import sys
N, M = map(int, input().split())

myDict = dict()
for i in range(N):
    site, password = sys.stdin.readline().rstrip().split()
    myDict[site] = password
for i in range(M):
    site = sys.stdin.readline().rstrip()
    print(myDict[site])