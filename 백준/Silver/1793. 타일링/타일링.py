DP = [0] * 251
DP[0] = 1
DP[1] = 1

for i in range(2, 251):
    DP[i] = DP[i-1] + DP[i-2]*2

while True:
    try:
        n = int(input())
        print(DP[n])
    except EOFError:
        break
