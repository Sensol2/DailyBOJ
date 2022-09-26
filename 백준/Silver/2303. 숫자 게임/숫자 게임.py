def GetBestValue(arr):
    sets = []
    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                value = arr[i] + arr[j] + arr[k]
                sets.append(str(value)[-1])
    return int(max(sets))


N = int(input())
winner = 0
best_score = -1
for i in range(N):
    arr = list(map(int, input().split()))
    score = GetBestValue(arr)
    if score >= best_score:
        best_score = score
        winner = i
print(winner+1)
