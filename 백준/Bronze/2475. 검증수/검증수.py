M = list(map(int, input().split()))
sum = 0
for i in M:
    sum += i*i
print(sum % 10)