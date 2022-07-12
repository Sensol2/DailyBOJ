n, k = map(int, input().split())
coins = []

for i in range(n):
    coins.append(int(input()))
coins = sorted(coins)

# 10001 : 만들 수 없는 경우
DP = [10001] * (k+1)
DP[0] = 0

for coin in coins:
    for i in range(k+1):
        if i % coin == 0:
            DP[i] = i//coin
        else:
            if coin + i <= k:
                DP[coin+i] = min(DP[coin+i], DP[i]+1)

if DP[k] != 10001:
    print(DP[k])
else:
    print("-1")
