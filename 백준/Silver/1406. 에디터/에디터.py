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

left = []
right = []
s = list(sys.stdin.readline().rstrip())
cursor = len(s)
left = s
num = int(sys.stdin.readline())
for i in range(num):
    command = sys.stdin.readline().rstrip()
    if command == 'L': # 커서 왼쪽으로 이동
        if 0 < cursor:
            right.append(left[len(left)-1])
            left.pop(len(left)-1)
            cursor -= 1
    if command == 'D': # 커서 오른쪽으로 이동
        if right:
            left.append(right[len(right)-1])
            right.pop(len(right)-1)
            cursor += 1
    # ABC 
    if command == 'B': # 커서 왼쪽 문자 삭제
        if 0 < cursor:
            left.pop(len(left)-1)
            cursor -= 1
    if 'P' in command: #커서 왼쪽에 문자 추가
        a, ch = command.split(' ')
        left.append(ch)
        # s.insert(cursor, ch)
        cursor += 1
right = list(reversed(right))
print(''.join(left+right))