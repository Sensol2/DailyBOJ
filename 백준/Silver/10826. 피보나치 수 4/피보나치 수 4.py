import sys

sys.setrecursionlimit(10000)


def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if DP[n] != 0:
        return DP[n]
    return fibo(n-2) + fibo(n-1)


N = int(input())
DP = [0]*10001
for i in range(1, 10001):
    DP[i] = fibo(i)
print(DP[N])
