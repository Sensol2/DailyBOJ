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

queue = []

def push(num):
    queue.append(num)

def pop():
    if isEmpty() == 1:
        return -1
    else:
        tmp = queue[0]
        queue.pop(0)
        return tmp

def size():
    return len(queue)

def isEmpty():
    if not queue:
        return 1
    if queue:
        return 0

def front():
    if isEmpty() == 1:
        return -1
    else:
        return queue[0]

def back():
    if isEmpty() == 1:
        return -1
    else:
        return queue[len(queue)-1]

commandsCnt = int(sys.stdin.readline())

for i in range(commandsCnt):
    command = sys.stdin.readline().strip()
    if 'push' in command:
        command, num = command.split(' ')
        push(num)

    if 'pop' in command:
        print(pop())

    if 'size' in command:
        print(size())

    if 'empty' in command:
        print(isEmpty())

    if 'front' in command:
        print(front())
    
    if 'back' in command:
        print(back())