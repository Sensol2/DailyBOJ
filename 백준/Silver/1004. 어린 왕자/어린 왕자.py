import math


def isInCircle(x, y, cx, cy, r):
    d = math.sqrt((x-cx)**2 + (y-cy)**2)
    if d < r:
        return True
    else:
        return False


T = int(input())
for i in range(T):
    # 입력부
    start_x, start_y, end_x, end_y = map(int, input().split())
    n = int(input())
    planets = []
    for j in range(n):
        cx, cy, r = map(int, input().split())
        planets.append((cx, cy, r))

    count = 0
    for planet in planets:
        cx, cy, r = planet

        startInCircle = isInCircle(start_x, start_y, cx, cy, r)
        endInCircle = isInCircle(end_x, end_y, cx, cy, r)
        if startInCircle and endInCircle:
            continue
        elif startInCircle or endInCircle:
            count += 1
    print(count)
