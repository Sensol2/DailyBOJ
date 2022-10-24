def fibo(n):
    if n <= 1:
        return n
    if DP[n]:
        return DP[n]
    DP[n] = fibo(n-1) + fibo(n-2)
    return DP[n]


n = int(input())
DP = [0, 1] + [0]*n

print(fibo(n))
