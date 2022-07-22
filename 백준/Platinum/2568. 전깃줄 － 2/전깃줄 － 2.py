def BinarySearch(start, end, num):
    if start == end:
        return start

    mid = (start + end) // 2

    if num <= DP[mid]:
        end = mid
    if DP[mid] < num:
        start = mid + 1

    res = BinarySearch(start, end, num)
    return res


n = int(input())
lines = []
for i in range(n):
    a, b = map(int, input().split())
    lines.append([a, b])


lines = sorted(lines, key=lambda x: x[0])


DP = []
indexorder = []
for idx, line in enumerate(lines):
    if idx == 0:
        DP.append(line[1])

    index = BinarySearch(0, len(DP), line[1])
    if len(DP) <= index:
        DP.append(line[1])
    else:
        DP[index] = line[1]
    indexorder.append([index, line])


max_index = len(DP) - 1

result = []
for i in range(len(indexorder)-1, -1, -1):
    if indexorder[i][0] == max_index:
        max_index -= 1
    else:
        result.append(indexorder[i])

print(len(result))
result = sorted(result, key=lambda x: x[1][0])
for rest in result:
    print(rest[1][0])
