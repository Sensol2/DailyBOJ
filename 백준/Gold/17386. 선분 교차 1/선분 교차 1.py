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


def Intersect(A, B, C, D):
    if CCW(A, C, D) != CCW(B, C, D) and CCW(A, B, C) != CCW(A, B, D):
        return 1
    return 0


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

A1 = Point(x1, y1)
A2 = Point(x2, y2)
B1 = Point(x3, y3)
B2 = Point(x4, y4)
print(Intersect(A1, A2, B1, B2))
