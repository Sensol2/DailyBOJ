students = [False] * 31

for i in range(28):
    num = int(input())
    students[num] = True

result = []
for i in range(1, 31):
    if students[i] == False:
        result.append(i)
print(min(result))
print(max(result))
