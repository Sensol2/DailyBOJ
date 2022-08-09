T = int(input())

DP = [[] for _ in range(10)]
DP[0] = [10]
for i in range(1, 10):
    for j in range(1, 10):
        num = str(i**j)[-1]
        if num not in DP[i]:
            DP[i].append(num)

for i in range(T):
    a, b = map(int, input().split())
    print(DP[a % 10][b % len(DP[a % 10])-1])
