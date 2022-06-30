def Calculator(n, depth, history):

    if n == 1:
        return (depth, history + [1])
    if DP[n]:
        return (DP[n][0] + depth, history + DP[n][1])

    best = []
    depth += 1
    history.append(n)
    if n % 3 == 0:
        best.append(Calculator(n//3, depth, history))
    if n % 2 == 0:
        best.append(Calculator(n//2, depth, history))
    if n-1 > 0:
        best.append(Calculator(n-1, depth, history))
    return min(best)


N = int(input())
DP = [None]*(N+1)

for i in range(1, N+1):
    res = Calculator(i, 0, [])
    DP[i] = res

print(DP[N][0])
print(' '.join(map(str, DP[N][1])))
