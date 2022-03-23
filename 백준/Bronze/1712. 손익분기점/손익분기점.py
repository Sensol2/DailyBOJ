import sys, time

a, b, c = map(int,sys.stdin.readline().split())

num = 0
if b >= c:
    num = -1
else:
    num = a // (c - b) + 1
print(num)