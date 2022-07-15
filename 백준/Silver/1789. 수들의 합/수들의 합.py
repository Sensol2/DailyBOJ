S = int(input())

DP = [0] * 200000
for i in range(1, 200000):
    DP[i] = DP[i-1] + i


for i in range(200000):
    if DP[i] > S:
        print(i-1)
        break
