results = []


def BackTracking(lst, idx, depth):
    if depth >= M:
        results.append(lst)
        return
    for i in range(idx, N):
        BackTracking(lst + [arr[i]], i+1, depth+1)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)
BackTracking([], 0, 0)
for result in results:
    print(' '.join(map(str, result)))