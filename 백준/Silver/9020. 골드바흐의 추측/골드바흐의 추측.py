def GeneratePrimeNumber(size):
    primes = [True] * size
    primes[0] = False
    primes[1] = False

    prime_set = []
    for i in range(2, size):
        if primes[i]:
            prime_set.append(i)
            for j in range(i*2, size, i):
                primes[j] = False

    return prime_set


primes = GeneratePrimeNumber(10000)
partition = dict()

for i in range(len(primes)):
    for j in range(i, len(primes)):
        key = primes[i] + primes[j]
        partition[key] = [primes[i], primes[j]]

T = int(input())
for i in range(T):
    N = int(input())
    print(' '.join(map(str, partition[N])))
