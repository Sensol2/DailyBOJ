import math

N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = math.inf
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_value = cards[i] + cards[j] + cards[k]
            if M < sum_value:
                continue
            else:
                result = min(result, M-sum_value)
print(M - result)