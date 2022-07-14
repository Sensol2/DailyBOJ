import heapq
N = int(input())
for i in range(N):
    arr = list(map(int, input().split()))
    heap = []
    for num in arr:
        heapq.heappush(heap, (-num, num))
    heapq.heappop(heap)
    heapq.heappop(heap)
    print(heapq.heappop(heap)[1])