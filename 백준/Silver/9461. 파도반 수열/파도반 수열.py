T = int(input())

for i in range(T):
    N = int(input())
    if N <= 3:
        print("1")
    else:
        DP = [0] * (N+1)
        DP[1] = 1
        DP[2] = 1
        DP[3] = 1

        for i in range(4, N+1):
            DP[i] = DP[i-3] + DP[i-2]
        print(DP[N])