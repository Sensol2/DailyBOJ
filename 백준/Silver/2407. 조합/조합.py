import math
N, M = map(int, input().split())

result = math.factorial(N) // (math.factorial(M) * math.factorial(N-M))
print(int(result))