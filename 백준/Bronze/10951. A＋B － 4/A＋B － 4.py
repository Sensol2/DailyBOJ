import sys

while True:
	try:
		n, x = map(int,sys.stdin.readline().split())
		print(n+x)
	except:
		break
