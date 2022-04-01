N = int(input())
DP = [0] * (N+1)

DP[1] = 1
for i in range(2, N+1):
    minValue = []

    for j in range(1, i):
        if i - j*j >= 0:
            minValue.append(DP[i - j*j] + 1)
        else:
            break
    DP[i] = min(minValue)

print(DP[N])