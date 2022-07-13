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
indexorder = []  # [삽입된 숫자, 삽입된 인덱스]를 저장
# 일반적인 LIS 알고리즘은 최대 길이만 구할 수 있고, 원본 SET은 보장되지 않기 때문에 필요

for idx, num in enumerate(arr):
    if idx == 0:
        result.append(arr[0])
        indexorder.append([arr[0], 0])
        continue

    res = BinarySearch(0, len(result), num, result)
    if len(result) <= res:
        result.append(num)
    else:
        result[res] = num
    indexorder.append([num, res])

# 단순히 최대 길이만 출력
print(len(result))

# 삽입된 인덱스의 역순에 따라 차례로 출력
# 이분탐색(nlogn) 에서 SET 을 구하기 위한 방법
max_index = len(result) - 1
LIS_SET = []
for index in reversed(indexorder):
    if index[1] == max_index:
        LIS_SET += [index[0]]
        max_index -= 1
    if max_index < 0:
        break

print(' '.join(map(str, reversed(LIS_SET))))
