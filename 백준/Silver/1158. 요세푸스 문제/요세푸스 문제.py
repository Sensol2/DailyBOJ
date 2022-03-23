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

n, k = map(int,sys.stdin.readline().split())

arr = list(range(1,n+1))
result = []
cnt = 0
i = 0
while arr:
    if i == len(arr):
        i = 0
        continue
    cnt += 1
    if cnt == k:
        result.append(arr[i])
        arr.pop(i)
        cnt = 0
        continue
    i += 1
print(str(result).replace("[", "<").replace("]",">"))