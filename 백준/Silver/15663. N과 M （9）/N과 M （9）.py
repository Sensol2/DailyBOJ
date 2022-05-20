
def DFS(arr, set):
    if len(arr) == M:
        if str(arr) not in DP.keys():
            DP[str(arr)] = True
            print(' '.join(map(str, arr)))
        return

    for i in range(len(set)):
        arr.append(set[i])
        tmp = set[:]
        tmp.pop(i)
        DFS(arr, tmp)
        arr.pop()


DP = dict()
N, M = map(int, input().split())
numset = list(map(int, input().split()))
numset = sorted(numset)

DFS([], numset)
