N, K = map(int, input().split())
coins = []
count = 0
for i in range(N):
    coins.append(int(input()))

coins.sort(reverse = True)

for i in coins:
    if i <= K:
        count += K // i
        K = K % i
print(count)