import math


def combination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))


T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    print(combination(M, N))
