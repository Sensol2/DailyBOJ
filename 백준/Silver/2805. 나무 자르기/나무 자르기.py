import math
result = (0, math.inf)


def BinarySearch(start, end):
    global result
    mid = (start + end) // 2
    if start == mid:
        return

    gain = 0
    for t in trees:
        if mid < t:
            cut = t - mid
            gain += cut

    if gain < M:  # 나무가 적으면
        BinarySearch(start, mid)  # 절단기 낮추기
    else:  # 나무가 충분하면
        if gain < result[1]:
            result = (mid, gain)
        BinarySearch(mid, end)  # 절단기 높이기


N, M = map(int, input().split())
trees = list(map(int, input().split()))

max_tree = max(trees)
BinarySearch(0, max_tree)
print(result[0])
