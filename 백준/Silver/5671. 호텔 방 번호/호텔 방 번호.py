while True:
    try:
        N, M = map(int, input().split())
        count = 0
        for i in range(N, M+1):
            sets = []
            flag = True
            for ch in str(i):
                if ch not in sets:
                    sets.append(ch)
                else:
                    flag = False
                    break
            if flag:
                count += 1
        print(count)
    except EOFError:
        break
