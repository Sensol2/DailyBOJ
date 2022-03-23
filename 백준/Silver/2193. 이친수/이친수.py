# 파이썬 문제풀이용 환경세팅
# [라이브러리]
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

dp = dict()
num = int(input())
dp[0] = 0
dp[1] = 1
dp[2] = 1

for i in range(3, num+1):
    sum_value = 0
    j = 1
    while j < i-1: 
        sum_value += dp[j]
        j += 1
    dp[i] = sum_value + 1

print(dp[num])
