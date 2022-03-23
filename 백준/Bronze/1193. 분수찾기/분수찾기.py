import sys, time

num = int(sys.stdin.readline())

prev = 1
level = 0
spare = 0
for i in range(10000000):
    d = 1 + (i-1)
    a = prev + d

    if num < a:
        level = i
        spare = num - prev
        break

    prev = a


if level % 2 == 0:
    front = 1
    back = level

    for i in range(spare):
        front += 1
        back -= 1
    print("%d/%d" % (front, back))
elif level % 2 != 0:
    front = level
    back = 1

    for i in range(spare):
        front -= 1
        back += 1
    print("%d/%d" % (front, back))