import sys
import math
input = sys.stdin.readline

def divideOrMinus(arr):
    for i in range(N):
        if arr[i] % 2 == 0:
            continue
        else:
            arr[i] -= 1
            return arr

    for i in range(N):
        arr[i] //= 2

    return arr

N = int(input())
B = list(map(int, input().split()))
A = [0] * N
count = 0

while A != B:
    arr = divideOrMinus(B)
    count += 1
print(count)