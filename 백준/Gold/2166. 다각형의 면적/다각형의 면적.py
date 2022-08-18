N = int(input())
points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append([x, y])
points.append(points[0])  # margin

sum_value_a = 0
for i in range(N):
    sum_value_a += points[i][0]*points[i+1][1]
sum_value_b = 0
for i in range(N):
    sum_value_b += points[i][1]*points[i+1][0]
result = abs(sum_value_a - sum_value_b) / 2
print("%.1f" % result)
