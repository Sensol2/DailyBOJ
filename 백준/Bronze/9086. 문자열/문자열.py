n = int(input())

for i in range(n):
    ch = input().rstrip()
    print(ch[0], ch[-1], sep='')
