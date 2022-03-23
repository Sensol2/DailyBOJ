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

s = list(sys.stdin.readline())

for c in s:
    if 'a' <= c and c <= 'z':
        ROT13 = chr(ord(c)+13)
        if 'a' <= ROT13 and ROT13 <= 'z':
            print(ROT13, end='')
        else:
            print(chr(ord('a')-1 + ord(ROT13) - ord('z')), end='')
    elif 'A' <= c and c <= 'Z':
        ROT13 = chr(ord(c)+13)
        if 'A' <= ROT13 and ROT13 <= 'Z':
            print(ROT13, end='')
        else:
            print(chr(ord('A')-1 + ord(ROT13) - ord('Z')), end='')
    else:
        print(c, end='')
