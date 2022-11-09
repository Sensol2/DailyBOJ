T = int(input())
for i in range(T):
    n = int(input())
    tmp = "".join(reversed(str(bin(n))[2:]))

    for i in range(len(tmp)):
        if tmp[i] == '1':
            print(i, end=' ')
