import math


def Sol(n):
    if n == 0:
        print("NO")
        return

    for i in range(20, -1, -1):
        if n >= math.factorial(i):
            n -= math.factorial(i)
    if n == 0:
        print("YES")
    else:
        print("NO")


N = int(input())
Sol(N)
