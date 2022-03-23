import sys, time

num = int(sys.stdin.readline())

d = 1
prevA = 0
for i in range(1,1000000000):
    a = prevA + d
    if a >= num:
        print(i)
        break
    d = 6 + 6*(i-1)
    prevA = a