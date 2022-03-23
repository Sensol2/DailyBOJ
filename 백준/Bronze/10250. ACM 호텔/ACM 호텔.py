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
for i in range(num):
    h, w, n = map(int,sys.stdin.readline().split())
    y = str(n%h)
    x = n//h + 1

    if y == '0': #꼭대기층
        x = n//h
        y = str(h)
    
    if x < 10:   #x가 한자리수면 0 붙이기
        x = "0" + str(x)
    else:
        x = str(x)
    print("%s%s" %(y,x))