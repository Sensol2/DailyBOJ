DP = [1] * 251


for i in range(2, 251):
    DP[i] = DP[i-1] + DP[i-2] + DP[i-2]

while True:
    try:
        n = int(input())
        print(DP[n])
    except EOFError:
        break
