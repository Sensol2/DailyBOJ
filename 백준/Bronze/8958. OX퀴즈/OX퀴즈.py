import sys, time
num = int(sys.stdin.readline())

for i in range(num):
	pattern = list(sys.stdin.readline())

	combo = 0
	score = 0

	for j in pattern:
		if j == 'O':
			combo += 1
			score += combo
		if j == 'X':
			combo = 0
	print(score)