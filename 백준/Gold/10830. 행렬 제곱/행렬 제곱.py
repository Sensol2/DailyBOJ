def matrix_mult(A, B):
    matrix = [[0] * len(A) for _ in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B[0])):
                matrix[i][k] += A[i][j] * B[j][k]

    for i in range(len(A)):
        for j in range(len(B[0])):
            matrix[i][j] %= 1000

    return matrix


def matrix_pow(A, n):
    if n == 1:  # 지수가 1인 경우
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] %= 1000
        return A

    if n % 2 == 0:
        res = matrix_pow(A, n//2)
        return matrix_mult(res, res)
    else:
        res = matrix_pow(A, n-1)
        return matrix_mult(res, A)


N, B = map(int, input().split())
A = [[0]*N for _ in range(N)]
for i in range(N):
    A[i] = list(map(int, input().split()))


resultMatrix = matrix_pow(A, B)

for i in range(len(A)):
    for j in range(len(A[0])):
        print(resultMatrix[i][j], end=' ')
    print()
