import sys
import math
n = int(input())

DP = [0] * 50001
DP[1] = 1
DP[2] = 2

for i in range(3, 50001):
    start = math.floor(math.sqrt(i))
    bestValue = []
    for j in range(start, 0, -1):
        value = 1 + DP[i - (j**2)]
        bestValue.append(value)
    DP[i] = min(bestValue)
print(DP[n])