import math


def Sol(n):
    if n == 0:
        print("NO")
        return

    limit = 10000000
    while True:
        for i in range(limit):
            if n < math.factorial(i+1):
                n -= math.factorial(i)
                limit = i
                break
            if i == limit - 1:
                n -= math.factorial(i)
                limit = i
                break

        if n == 0:
            print("YES")
            return

        if limit == 0:
            if n == 0:
                print("YES")
            else:
                print("NO")
            return


N = int(input())
Sol(N)
