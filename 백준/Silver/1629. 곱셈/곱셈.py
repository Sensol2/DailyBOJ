def power(a, b):
    if b == 0:
        return 1

    res = power(a, b//2)
    if b % 2 == 0:  # 지수가 짝수인 경우
        return res*res % C
    else:  # 지수가 홀수인 경우
        return res*res * a % C


A, B, C = map(int, input().split())
print(power(A, B))
