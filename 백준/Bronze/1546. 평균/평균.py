import sys, time
num = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
best = max(scores)
for i, v in enumerate(scores):
	scores[i] = v / best * 100
print(sum(scores)/num)