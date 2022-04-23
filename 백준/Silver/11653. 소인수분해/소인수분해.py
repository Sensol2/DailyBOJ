def Factorization(N):
    for i in range(2, N+1):
        if N % i == 0:
            return [i, N // i]

N = int(input())

res = []

while N != 1:
    item = Factorization(N)
    primeFactor, new_N = item[0], item[1]
    res.append(primeFactor)
    N = new_N

for i in res:
    print(i)