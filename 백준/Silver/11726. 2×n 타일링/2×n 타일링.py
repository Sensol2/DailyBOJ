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
    if dpList[n-2] and dpList[n-1]:
        dpList[n] = dpList[n-2] + dpList[n-1]

num = int(sys.stdin.readline())

dpList[0] = 0
dpList[1] = 1
dpList[2] = 2

for i in range(2, num+1):
    CalcTiles(i)

print(dpList[num] % 10007)