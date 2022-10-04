import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
    command = int(input())

    if command == 0:
        if heap:
            item = heapq.heappop(heap)
            print(item[1])
        else:
            print("0")
    else:
        heapq.heappush(heap, [-command, command])
