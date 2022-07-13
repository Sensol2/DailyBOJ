def BinarySearch(start, end, num, arr):  # 이분 탐색 활용, num 이 들어갈 인덱스를 반환
    if start == end:
        return start

    mid = (start + end) // 2

    if num <= arr[mid]:
        end = mid
    elif arr[mid] < num:
        start = mid + 1

    res = BinarySearch(start, end, num, arr)
    return res


N = int(input())
arr = list(map(int, input().split()))
result = []


for idx, num in enumerate(arr):
    if idx == 0:
        result.append(arr[0])
        continue

    res = BinarySearch(0, len(result), num, result)
    if len(result) <= res:
        result.append(num)
    else:
        result[res] = num

count = 0
for r in result:
    if r:
        count += 1
print(count)
