import re


arr = []
for i in range(5):
    num = int(input())
    if num < 40:
        num = 40
    arr.append(num)
print(sum(arr)//5)