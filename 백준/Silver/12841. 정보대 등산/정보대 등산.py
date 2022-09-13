import math
import sys

input = sys.stdin.readline


def GeneratePrefixSum(arr):
    size = len(arr)
    DP = [0] * size
    DP[0] = arr[0]
    for i in range(1, size):
        DP[i] = DP[i-1] + arr[i]
    return DP


n = int(input())
cross = list(map(int, input().split()))
leftSide = list(map(int, input().split()))
rightSide = list(map(int, input().split()))
lPrefixSum = [0] + GeneratePrefixSum(leftSide)
rPrefixSum = [0] + GeneratePrefixSum(rightSide)

best_value = math.inf
best_set = None
for i in range(len(cross)):
    left_cost = lPrefixSum[i]
    right_cost = rPrefixSum[n-1] - rPrefixSum[i]
    total_cost = cross[i] + left_cost + right_cost
    if total_cost < best_value:
        best_value = total_cost
        best_way = i+1
print(best_way, best_value)
