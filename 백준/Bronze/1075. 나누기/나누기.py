N = input()
F = int(input())

for i in range(100):
    if i < 10:
        num = int(N[:len(N)-2] + "0" + str(i))
        if num % F == 0: 
            print("0", i, sep='')
            break
    else:
        num = int(N[:len(N)-2] + str(i))
        if num % F == 0: 
            print(i, sep='')
            break