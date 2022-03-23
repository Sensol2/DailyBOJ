import sys, time

t = int(sys.stdin.readline())
for i in range(t):
	r, s = sys.stdin.readline().split()
	splited = list(s)
	for j in s:
		for k in range(int(r)):
			print(j, end='')
	print()