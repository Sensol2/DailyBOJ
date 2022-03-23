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
	a.reverse()

	ap = a[1] - a[0]
	for i in range(0, len(a)-1):
		if a[i] != a[i+1] - ap:
			return False
	return True

count = 0
num = int(sys.stdin.readline())
for i in range(1, num+1):
	if Sum_of_each_digit(i) == True:
		count += 1
print(count)