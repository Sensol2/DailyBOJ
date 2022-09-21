from re import A


N, M = map(int, input().split())
matrix_a = []
for i in range(N):
    matrix_a.append(list(map(int, input().split())))
M, K = map(int, input().split())
matrix_b = []
for i in range(M):
    matrix_b.append(list(map(int, input().split())))

new_arr = []
for k in range(K):
    tmp = []
    for m in range(M):
        tmp.append(matrix_b[m][k])
    new_arr.append(tmp)
matrix_b = new_arr

result = [[0] * len(matrix_b) for _ in range(len(matrix_a))]
for i in range(len(matrix_a)):
    for j in range(len(matrix_b)):
        res = 0
        for k in range(len(matrix_a[i])):
            res += matrix_a[i][k] * matrix_b[j][k]
        result[i][j] = res

for row in result:
    for a in row:
        print(a, end=' ')
    print()
# -1 -2 6
# -3 -6 12
# -5 -10 18
