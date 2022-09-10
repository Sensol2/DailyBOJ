N, K = map(int, input().split())

isPrime = [True] * (N+1)
isPrime[0] = False
isPrime[1] = False

count = 0
for i in range(2, N+1):
    if isPrime[i]:
        count += 1
        if count == K:
            print(i)
        for j in range(i*2, N+1, i):
            if isPrime[j]:
                isPrime[j] = False
                count += 1
                if count == K:
                    print(j)
