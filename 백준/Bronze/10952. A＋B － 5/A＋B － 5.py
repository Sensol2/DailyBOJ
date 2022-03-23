import sys

while True:
	n, x = map(int,sys.stdin.readline().split())
	if (n == 0 and x == 0):
		break
	print(n+x)