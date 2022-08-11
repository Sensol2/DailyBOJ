def TwoPointer(M):  # 두 원소의 부분합이 정확히 M이 되는 경우를 찾는다
    s = 0
    e = 0
    count = 0
    S = 0

    while True:
        if e == N:
            while s < e:
                S -= arr[s]
                s += 1
                if S == M:
                    count += 1
            break

        if S < M:
            e += 1
            S += arr[e-1]  # 새로 포함한 원소 더하기
        elif S >= M:
            S -= arr[s]
            s += 1

        if S == M:
            count += 1

    return count


N, M = map(int, input().split())
arr = list(map(int, input().split()))
print(TwoPointer(M))
