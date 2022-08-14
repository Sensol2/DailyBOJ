import math

N = int(input())
arr = list(map(int, input().split()))
base = []  # 알칼리성, -
acid = []  # 산성, +
for num in arr:
    if num < 0:
        base.append(num)
    else:
        acid.append(num)


min_value = math.inf
result = []
if len(base) >= 2:  # 알칼리 용액만으로 만드는 경우
    if abs(base[-2] + base[-1]) < min_value:
        min_value = abs(base[-2] + base[-1])
        result = [base[-2], base[-1]]
if len(acid) >= 2:  # 산성 용액만으로 만드는 경우
    if abs(acid[0] + acid[1]) < min_value:
        min_value = abs(acid[0] + acid[1])
        result = [acid[0], acid[1]]

for b in base:
    prev = math.inf  # 이전 용액
    for a in acid:
        if prev < abs(b+a):  # 이전 용액보다 기록이 안좋으면 탈출
            break
        if abs(b+a) < min_value:
            min_value = abs(b+a)
            result = [b, a]
        prev = abs(b+a)

print(' '.join(map(str, result)))
