n, k = map(int, input().split())
coins = []

for i in range(n):
    coins.append(int(input()))
coins = sorted(coins)
# 가치가 작은 순부터 정렬

# 10001: 만들 수 없는 경우
DP = [0] * (k+1)
DP[0] = 0

for coin in coins:
    for i in range(k+1):
        if DP[i] == 0:
            if i % coin == 0:
                DP[i] = 1
            continue

        if i != 0:
            DP[0] = 1

        if i + coin <= k:
            DP[i+coin] += DP[i]

print(DP[k])