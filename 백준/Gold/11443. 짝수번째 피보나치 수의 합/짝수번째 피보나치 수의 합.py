def matrix_mult(A, B):
    matrix = [[0] * len(A) for _ in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B[0])):
                matrix[i][k] += A[i][j] * B[j][k]

    for i in range(len(A)):
        for j in range(len(B[0])):
            matrix[i][j] %= 1000000007

    return matrix


def matrix_pow(A, n):
    if n == 0:
        return [[0, 0], [0, 0]]
    if n == 1:  # 지수가 1인 경우
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] %= 1000000007
        return A

    if n % 2 == 0:
        res = matrix_pow(A, n//2)
        return matrix_mult(res, res)
    else:
        res = matrix_pow(A, n-1)
        return matrix_mult(res, A)


N = int(input())
mat = [[1, 1], [1, 0]]
sum_v = 0

if N % 2 != 0:  # 홀수
    resultMatrix = matrix_pow(mat, N)
else:
    resultMatrix = matrix_pow(mat, N + 1)
sum_v = resultMatrix[0][1] - 1
print(sum_v)
