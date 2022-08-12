results = []


def BackTracking(lst, depth):
    if depth >= M:
        results.append(lst)
        return
    for n in arr:
        BackTracking(lst + [n], depth+1)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)

for n in arr:
    BackTracking([n], 1)
for result in results:
    print(' '.join(map(str, result)))
