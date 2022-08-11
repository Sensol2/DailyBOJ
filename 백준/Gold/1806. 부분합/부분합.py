import math


def TwoPointer(M):  # 두 원소의 부분합이 정확히 M이 되는 경우를 찾는다
    s = 0
    e = 0
    S = 0
    result = math.inf
    while True:
        if e == N:
            while s < e:
                if S >= M and e - s < result:
                    result = e - s
                S -= arr[s]
                s += 1

            break

        if S < M:
            e += 1
            S += arr[e-1]  # 새로 포함한 원소 더하기
        elif S >= M:
            if e - s < result:
                result = e - s

            S -= arr[s]
            s += 1

    return result


N, M = map(int, input().split())
arr = list(map(int, input().split()))

r = TwoPointer(M)
if r == math.inf:
    print(0)
else:
    print(r)
