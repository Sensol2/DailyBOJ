def GCD(A, B):
    if A % B == 0:
        return B
    else:
        return GCD(B, A % B)


A, B = map(int, input().split())
print((A*B) // GCD(A, B))
