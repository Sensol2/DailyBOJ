N, M = map(int, input().split())

arr = list(map(int, input().split()))

best = 999999
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_value = arr[i] + arr[j] + arr[k]
            if abs(M - sum_value) < abs(M - best) and sum_value <= M :
                best = sum_value
print(best)