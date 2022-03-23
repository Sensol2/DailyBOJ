# 파이썬 문제풀이용 환경세팅
# [라이브러리]
from calendar import c
import sys, time
import math

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~파도가 친다 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# [자주 쓰는 입력 모듈]
# 1) 정수 한 개 입력
# num = int(sys.stdin.readline())
# 2) 여러개 입력
# a, b, c = map(int,sys.stdin.readline().split())
# 3) 여러개 리스트로 입력
# arr = list(map(int,sys.stdin.readline().split()))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~파도가 친다 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

count = 0
arr = dict()
def dp(n):
    global count
    if n in arr.keys():
        return arr[n]
    count += 1
    best = []
    if n % 3 == 0:
        best.append(dp(n//3))
    if n % 2 == 0:
        best.append(dp(n//2))
    best.append(dp(n-1))
    arr[n] = min(best) + 1

arr[0] = 0
arr[1] = 0
arr[2] = 1
arr[3] = 1

num = int(sys.stdin.readline())
for i in range(1, num+1):
    dp(i)
print(dp(num))