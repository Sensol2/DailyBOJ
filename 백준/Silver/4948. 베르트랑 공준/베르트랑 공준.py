def generatePrimeNumber(size):
    primes = []
    isPrime = [True] * (size+1)

    for i in range(2, size):
        if isPrime[i]:
            primes.append(i)
        for j in range(i*2, size, i):
            isPrime[j] = False
            

    return primes

primes = generatePrimeNumber(250000)

while True:
    n = int(input())
    if n == 0:
        break
    
    count = 0
    for prime in primes:
        if n < prime and prime <= n*2:
            count += 1

    print(count)