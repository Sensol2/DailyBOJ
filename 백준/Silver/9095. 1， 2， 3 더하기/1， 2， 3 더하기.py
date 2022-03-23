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
dpList = dict()

def CalcTiles(n):
    if dpList[n-3] and dpList[n-2] and dpList[n-1]:
        dpList[n] = dpList[n-3] + dpList[n-2] + dpList[n-1]



dpList[0] = 0
dpList[1] = 1
dpList[2] = 2
dpList[3] = 4
dpList[4] = 7

nums = []
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    nums.append(n)


for i in range(3, max(nums)+1):
    CalcTiles(i)

for i in range(t):
    print(dpList[nums[i]])