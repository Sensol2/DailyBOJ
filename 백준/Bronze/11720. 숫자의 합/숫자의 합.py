import sys, time

def Sum_of_each_digit (num):
	div = 10
	a = []
	while True:
		a.append(num % div)
		num = num // div
		if num // div == 0:
			a.append(num % div)
			break
	return sum(a)

num = int(sys.stdin.readline())
a = int(sys.stdin.readline())
print(Sum_of_each_digit(a))