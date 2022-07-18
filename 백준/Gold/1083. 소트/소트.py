def swap(arr, index_a, index_b):
    tmp = arr[index_a]
    arr[index_a] = arr[index_b]
    arr[index_b] = tmp


N = int(input())
arr = list(map(int, input().split()))
K = int(input())


for i in range(N):
    start = i+1
    end = start + K
    max_num = -1
    max_idx = i
    for j in range(start, end):
        if len(arr) <= j:  # 인덱스 초과 방지
            break
        if max_num < arr[j]:
            max_num = arr[j]
            max_idx = j

    if max_num <= arr[i]:
        continue

    for j in range(max_idx, i, -1):
        if arr[j-1] < arr[j]:
            swap(arr, j-1, j)
            K -= 1

for i in arr:
    print(i, end=' ')
