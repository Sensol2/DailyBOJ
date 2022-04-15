N, M = map(int, input().split())
arr = dict()
result = list()
for i in range(N+M):
    name = input()
    if name not in arr.keys():
        arr[name] = 0
    else:
        result.append(name)

result = sorted(result)
print(len(result))
for i in result:
    print(i)
