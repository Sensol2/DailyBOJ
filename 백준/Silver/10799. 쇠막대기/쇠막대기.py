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

stack = []


def size():
    return len(stack)

def isEmpty():
    if not stack:
        return 1
    if stack:
        return 0

def top():
    if isEmpty() == 1:
        return -1
    else:
        return stack[len(stack)-1]

def push(num):
    stack.append(num)

def pop():
    if isEmpty() == 1:
        return -1
    else:
        tmp = top()
        stack.pop(len(stack)-1)
        return tmp

inputs = list(sys.stdin.readline().strip())

prev = ''

stacked_LBracket = 0
stacked_RBracket = 0
laser = 0
result = 0
for i in inputs:
    push(i)

    if i == '(':
        stacked_LBracket += 1
    elif i == ')':
        if prev == '(': # ()패턴 발견되면 삭제
            pop()
            pop()
            stacked_LBracket -= 1
            result += stacked_LBracket
        else:
            stacked_LBracket -= 1
            result += 1
    prev = i

print(result)