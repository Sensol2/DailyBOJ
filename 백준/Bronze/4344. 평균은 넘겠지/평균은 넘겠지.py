import sys, time
num = int(sys.stdin.readline())

for i in range(num):
	scores = list(map(int,sys.stdin.readline().split()))
	scores.pop(0)
	avg = sum(scores) / len(scores)
	avgHighScores = list(filter(lambda x: x > avg, scores))
	print("%.3f%%" %(len(avgHighScores)/len(scores) * 100))