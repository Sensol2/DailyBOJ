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

deck = []

def push_front(num):
    deck.insert(0, num)

def push_back(num):
    deck.append(num)

def pop_front():
    if isEmpty() == 1:
        return -1
    else:
        tmp = deck[0]
        deck.pop(0)
        return tmp

def pop_back():
    if isEmpty() == 1:
        return -1
    else:
        tmp = deck[len(deck)-1]
        deck.pop(len(deck)-1)
        return tmp

def size():
    return len(deck)

def isEmpty():
    if not deck:
        return 1
    if deck:
        return 0

def front():
    if isEmpty() == 1:
        return -1
    else:
        return deck[0]

def back():
    if isEmpty() == 1:
        return -1
    else:
        return deck[len(deck)-1]

commandsCnt = int(sys.stdin.readline())

for i in range(commandsCnt):
    command = sys.stdin.readline().strip()
    if 'push_front' in command:
        command, num = command.split(' ')
        push_front(num)

    if 'push_back' in command:
        command, num = command.split(' ')
        push_back(num)

    if 'pop_front' == command:
        print(pop_front())

    if 'pop_back' == command:
        print(pop_back())

    if 'size' == command:
        print(size())

    if 'empty' == command:
        print(isEmpty())

    if 'front' == command:
        print(front())
    
    if 'back' == command:
        print(back())