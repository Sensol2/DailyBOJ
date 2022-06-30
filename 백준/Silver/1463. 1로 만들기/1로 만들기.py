def Calculator(n, depth):
    if n == 1:
        return depth
    if DP[n]:
        return DP[n] + depth

    best = []
    depth += 1
    if n % 3 == 0:
        best.append(Calculator(n//3, depth))
    if n % 2 == 0:
        best.append(Calculator(n//2, depth))
    if n-1 > 0:
        best.append(Calculator(n-1, depth))
    return min(best)


N = int(input())
DP = [None]*(N+1)

for i in range(1, N+1):
    res = Calculator(i, 0)
    DP[i] = res
print(DP[N])
