def DFS(arr, level):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(level, N+1):
        arr.append(i)
        DFS(arr, i)
        arr.pop()

N, M = map(int, input().split())

DFS([], 1)