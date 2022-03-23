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

arr = list(map(str,sys.stdin.readline().split()))

sum1 = arr[0] + arr[1]
sum2 = arr[2] + arr[3]
print(int(sum1)+int(sum2))