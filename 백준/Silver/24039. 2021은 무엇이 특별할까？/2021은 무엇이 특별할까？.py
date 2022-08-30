def GeneratePrimeNumber(size):
    DP = [False] * (size+1)
    primes = []

    for i in range(2, size):
        if not DP[i]:
            primes.append(i)
            for j in range(i*2, size, i):
                DP[j] = True
    return primes


N = int(input())

primes = GeneratePrimeNumber(110)
DP = []
for i in range(1, len(primes)):
    DP.append(primes[i-1] * primes[i])

for num in DP:
    if num > N:
        print(num)
        break
