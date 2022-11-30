n = int(input())

pisano_period = 15 * 10**5

fibo = [0] * pisano_period
fibo[0] = 0
fibo[1] = 1

for i in range(2, 1500000):
    fibo[i] = (fibo[i-2] + fibo[i-1]) % 1000000
print(fibo[n % pisano_period])
