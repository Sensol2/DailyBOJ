import sys, time
a = []
for i in range(10):
	num = int(sys.stdin.readline())
	if a.count(num % 42) == 0:
		a.append(num % 42)
print(len(a))