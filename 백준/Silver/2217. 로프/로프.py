import sys
import math
input = sys.stdin.readline

N = int(input())
ropes = []

for i in range(N):
    ropes.append(int(input()))
ropes = sorted(ropes, reverse=True)

result = []
for idx, rope in enumerate(ropes):
    x = rope * (idx+1)
    result.append(x)
print(max(result))
