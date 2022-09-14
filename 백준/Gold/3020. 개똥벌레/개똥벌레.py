import math
import sys
from collections import deque
input = sys.stdin.readline
N, H = map(int, input().split())

down_stone = [0]*H
up_stone = [0]*H

for i in range(N//2):
    down_stone[int(input())] += 1
    up_stone[int(input())] += 1

d_dp = [N//2] * (H+1)
# 아래 종유석부터 구하기
for h in range(H):
    d_dp[h+1] = d_dp[h] - down_stone[h]


u_dp = [N//2] * (H+1)
# 위 종유석 (뒤집었다고 생각하기)
for h in range(H):
    u_dp[h+1] = u_dp[h] - up_stone[h]

best_cost = math.inf
best_count = 0
for h in range(1, H+1):
    result = d_dp[h] + u_dp[H+1-h]
    if result == best_cost:
        best_count += 1
    elif result < best_cost:
        best_cost = result
        best_count = 1
print(best_cost, best_count)
