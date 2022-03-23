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

strList = []
for i in range(101):
    try:
        s = list(input())
        strList.append(s)
    except EOFError:
            break

for s in strList:
    a = b = c = d = 0 
    for ch in s:
        if ord('a') <= ord(ch) and ord(ch) <= ord('z'):
            a += 1
        if ord('A') <= ord(ch) and ord(ch) <= ord('Z'):
            b += 1
        if ord('0') <= ord(ch) and ord(ch) <= ord('9'):
            c += 1
        if ch == ' ':
            d += 1
    print("%d %d %d %d" %(a,b,c,d))

