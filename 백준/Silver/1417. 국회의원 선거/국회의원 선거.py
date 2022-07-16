def ElectoralFraud():
    count = 0
    while True:
        for i in range(1, N):
            rival = max(candidate[1:])
            if candidate[0] > rival:
                return count
            if candidate[i] == rival:
                candidate[i] -= 1
                candidate[0] += 1
                count += 1


N = int(input())
candidate = [0] * N
for i in range(N):
    candidate[i] = int(input())

if N > 1:
    print(ElectoralFraud())
else:
    print(0)
