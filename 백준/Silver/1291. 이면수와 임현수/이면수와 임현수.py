def GeneratePrimeNumber(size):  # 소수 생성기
    DP = [0] * size
    prime = []
    for i in range(2, size, 1):
        if not DP[i]:
            prime.append(i)
            for j in range(i*2, size, i):
                DP[j] = 1
    return prime


def isDigitOdd(n):  # 각 자릿수가 홀수인가?
    sum_value = 0
    for ch in str(n):
        sum_value += int(ch)
    if sum_value % 2 == 0:
        return False
    else:
        return True


def getPrimeFactor(n, primes):  # 소인수 분해
    factors = []
    for prime in primes:
        if n < prime:
            break

        count = 0
        while n % prime == 0:
            n //= prime
            count += 1
        if count > 0:
            factors.append([prime, count])
    return factors


def isCompositeNumber(n):  # 합성수 판별
    if 1 < n and n not in primes:
        return True
    return False


def isImyeonsu(n):  # 이면수 판별
    if 6 <= N and isDigitOdd(N):
        return True
    return False


def isImHyunsoo(n):  # 임현수 판별
    if N == 2 or N == 4 or (isCompositeNumber(N) and len(getPrimeFactor(N, primes)) % 2 == 0):
        return True
    return False


N = int(input())
primes = GeneratePrimeNumber(2700)
# 4. 이면수 and 임현수
if isImyeonsu(N) and isImHyunsoo(N):
    print(4)
# 1. 이면수
elif isImyeonsu(N):
    print(1)
# 2. 임현수
elif isImHyunsoo(N):
    print(2)
# 3. not 이면수 and not 임현수
elif not isImyeonsu(N) and not isImHyunsoo(N):
    print(3)
