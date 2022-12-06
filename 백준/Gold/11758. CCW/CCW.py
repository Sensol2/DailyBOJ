class Point():
    x = 0
    y = 0

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


def CCW(A, B, C):
    a = (A.x*B.y + B.x*C.y + C.x*A.y) - (B.x*A.y + C.x*B.y + A.x*C.y)
    if a < 0:  # 시계
        return -1
    if a == 0:  # 평행
        return 0
    if a > 0:  # 반시계
        return 1


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

X1 = Point(x1, y1)
Y1 = Point(x2, y2)
Z1 = Point(x3, y3)

print(CCW(X1, Y1, Z1))
