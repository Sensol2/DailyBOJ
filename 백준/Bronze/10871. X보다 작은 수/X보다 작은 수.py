import sys
n, x = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
filtered = list(filter(lambda t: t<x, a))

for i in filtered:
	print(i, end=' ')