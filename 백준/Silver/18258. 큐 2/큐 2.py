from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
queue = deque()
for i in range(N):
    command = input().rstrip()
    if " " in command:  # push
        a, b = command.split()
        queue.append(int(b))
        continue
    if command == "pop":
        if len(queue) > 0:
            a = queue.popleft()
            print(a)
        else:
            print(-1)
        continue
    if command == "size":
        print(len(queue))
        continue
    if command == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
        continue
    if command == "front":
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
        continue
    if command == "back":
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
        continue
