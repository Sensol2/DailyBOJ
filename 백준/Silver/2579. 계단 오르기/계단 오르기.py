N = int(input())
stairs = []
for i in range(N):
    stairs.append(int(input()))

if N <= 2:
    if N == 1:
        print(stairs[0])
    elif N == 2:
        print(stairs[0]+stairs[1])
else:
    DP = [0] * N
    DP[0] = stairs[0]
    DP[1] = stairs[0] + stairs[1]
    DP[2] = max(stairs[0], stairs[1]) + stairs[2]

    for i in range(3, N):
        DP[i] = max(stairs[i] + DP[i-2], stairs[i] + stairs[i-1] + DP[i-3])

    print(DP[len(DP)-1])