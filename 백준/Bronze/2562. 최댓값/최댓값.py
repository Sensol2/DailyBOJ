import sys, time

# num = list(map(int, sys.stdin.readline().split()))
a = []
for i in range(9):
	a.append(int(sys.stdin.readline()))
print(max(a))
print(a.index(max(a))+1)