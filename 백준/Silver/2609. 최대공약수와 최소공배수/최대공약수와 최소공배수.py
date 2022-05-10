N, M = map(int, input().split())

# 최대공약수, 최소공배수
gcd = 1
lcm = N*M

for i in range(1, max([N,M])+1):
    if N % i == 0 and M % i == 0:
        gcd = i

for i in range(0,(N*M)+1,gcd):
    if i == 0:
        continue
    if i % N == 0 and i % M == 0:
        lcm = i
        break

print(gcd)
print(lcm)
