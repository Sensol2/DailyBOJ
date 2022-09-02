def Backtracking(seq, idx):
    if seq and sum(seq) == S:
        global count
        count += 1

    for i in range(idx, len(arr)):
        next_lst = seq + [arr[i]]
        Backtracking(next_lst, i+1)
        next_lst.pop()


N, S = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
Backtracking([], 0)
print(count)
