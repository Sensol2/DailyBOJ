from heapq import *

arr = []
for i in range(8):
    num = int(input())
    heappush(arr, [-num, num, i+1])

scores = []
score_indexs = []
for i in range(5):
    item = heappop(arr)
    scores.append(item[1])
    score_indexs.append(item[2])


print(sum(scores))
print(' '.join(map(str, sorted(score_indexs))))
