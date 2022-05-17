def DFS(arr, numset):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return

    for i in numset:
        arr.append(i)
        tmp = numset[:]
        tmp.remove(i)
        DFS(arr, tmp)
        arr.pop()


N, M = map(int, input().split())
numset = list(map(int, input().split()))
numset = sorted(numset)
DFS([], numset)
