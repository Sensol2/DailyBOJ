DP = [0] * 20001

for i in range(10001):
    result = i
    parts = list(map(int, list(str(i))))
    for part in parts:
        result += part

    DP[result] = result

for i in range(1, 10001):
    if DP[i] == 0:
        print(i)
