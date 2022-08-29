def GCD(A, B):
    if A % B == 0:
        return B
    else:
        return GCD(B, A % B)


N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    print((A*B) // GCD(A, B))