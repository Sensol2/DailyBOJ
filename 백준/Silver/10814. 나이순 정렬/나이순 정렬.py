N = int(input())
arr = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    arr.append([age, name, i])

result = sorted(arr, key=lambda x: (x[0], x[2]))
for i in result:   
    print(i[0], i[1])