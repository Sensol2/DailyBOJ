import sys
import math
n = int(input())
num = math.factorial(n)
num = list(reversed(list(str(num))))
result = 0
for i in num:
    if i == '0':
        result += 1
    else:
        break
print(result)