import math
T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    # 피타고라스 정리에 따라 빗변 길이 구하기
    h = abs(x1 - x2)
    v = abs(y1 - y2)
    d = math.sqrt(h*h + v*v)
    rb = max([r1, r2])
    rs = min([r1, r2])

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif rb + rs == d or rb - rs == d:
        print(1)
    elif rb - rs < d and d < rb + rs:
        print(2)
    elif rb + rs < d or d < rb - rs or (d == 0 and rb != rs):
        print(0)

# CASE1:
# 무한대인 경우: 두 원이 같은 원인경우
# CASE2:
# 교점이 1개인 경우: 
# CASE3:
# 교점이 2개인 경우
# CASE4: 교점이 없는 경우
#  1) 두 원이 멀리 떨어져있거나
#  2) 한 원이 다른 원을 품었거나