def Calc():
    for i in range(N):
        sum = i
        chs = list(map(int, list(str(i))))
        for ch in chs:
            sum += ch

        if sum == N:
            return i
    return 0


N = int(input())

print(Calc())
