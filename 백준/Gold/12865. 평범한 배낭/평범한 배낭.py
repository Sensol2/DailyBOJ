def GrabMaximumValue(itemList, weight):
    value = [0, ]
    
    for idx, item in enumerate(itemList):
        if item[0] > weight:
            break
        else:
            if idx == 0:
                value.append(item[1])
            else:
                rest_w = weight - item[0]
                value.append(item[1] + DP[rest_w][idx-1])

            # value.append(item[1] + GrabMaximumValue(itemList[:idx], weight - item[0]))
    return max(value)


N, K = map(int, input().split())

DP = [[0]*N for _ in range(K+1)]
items = []
for i in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

# 무게에 따라 오름차순 정렬
items = sorted(items, key=lambda x: x[0])

for i in range(K+1):
    for j in range(N):
        DP[i][j] = GrabMaximumValue(items[:j+1], i)
print(max(DP[K]))