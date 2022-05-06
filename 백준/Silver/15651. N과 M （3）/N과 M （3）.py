res = []
def Backtracking(arr, N, M):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1,N+1):
        Backtracking(arr + [i], N, M)

N, M = map(int, input().split())
for i in range(1,N+1):
    Backtracking([i], N, M)