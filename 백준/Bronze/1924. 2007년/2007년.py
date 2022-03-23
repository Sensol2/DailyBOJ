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

a, b = map(int,sys.stdin.readline().split())

cal = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

totalDate = 0

sum = 0
for i in cal:
    if i == a:
        break
    sum += cal[i]
totalDate = sum + b

day = totalDate % 7
if day == 1:
    print("MON")
if day == 2:
    print("TUE")
if day == 3:
    print("WED")
if day == 4:
    print("THU")
if day == 5:
    print("FRI")
if day == 6:
    print("SAT")
if day == 0:
    print("SUN")

