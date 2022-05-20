
def DFS(arr, level):
    if len(arr) == M:
        if str(arr) not in DP.keys():
            DP[str(arr)] = True
            print(' '.join(map(str, arr)))
        return

    for i in range(level, len(numset)):
        arr.append(numset[i])
        DFS(arr, i)
        arr.pop()


DP = dict()
N, M = map(int, input().split())
numset = list(map(int, input().split()))
numset = sorted(numset)

DFS([], 0)
