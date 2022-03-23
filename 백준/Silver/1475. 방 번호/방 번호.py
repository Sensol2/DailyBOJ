from collections import deque
import sys, time
import math
N = list(input())
numcount = [0] * 10
for i in N:
    for j in range(0,10,1):
        if i == str(j):
            numcount[j] += 1

sumof6and9 = math.ceil((numcount[6] + numcount[9]) / 2)
numcount.pop(6)
numcount.pop(8)
numcount.append(sumof6and9)
print(max(numcount))