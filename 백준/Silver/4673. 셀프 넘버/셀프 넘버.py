import sys, time

selfnums = list(range(1, 10000))
for i in range(10000):
	num = i
	div = 10
	a = []
	while True:
		a.append(num % div)
		num = num // div
		if num // div == 0:
			a.append(num % div)
			break
	selfnum = i + sum(a)
	if selfnum in selfnums:
		selfnums.remove(selfnum)

for i in selfnums:
	print(i)