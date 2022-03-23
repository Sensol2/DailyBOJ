import sys, time

count = 0
n = int(sys.stdin.readline())

newNumber = n
while True:
	if count != 0 and newNumber == n:
		print(count)
		break

	first = newNumber // 10
	second = newNumber % 10
	newSecond = first + second
	newNumber = second * 10 + newSecond % 10
	count+=1


