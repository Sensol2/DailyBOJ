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


num = int(sys.stdin.readline())

isCannotCreate = False
Bag3kg = 0
while True:
    if num % 5 == 0:
        break
    if num == 0:
        break
    if num < 0:
        isCannotCreate = True
        break
    num -= 3
    Bag3kg += 1
Bag5kg = num // 5
if isCannotCreate:
    print("-1")
else:
    print(Bag3kg + Bag5kg)