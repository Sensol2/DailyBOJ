k = int(input())

numList = []
for i in range(k):
    num = int(input())
    if num != 0:
        numList.append(num)
    elif num == 0:
        numList.pop()
print(sum(numList))