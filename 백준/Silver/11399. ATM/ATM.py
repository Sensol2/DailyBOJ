N = int(input())

queue = list(map(int, input().split()))
queue.sort()
sum = 0
result = 0
while queue:
    sum += queue.pop(0)
    result += sum
print(result)