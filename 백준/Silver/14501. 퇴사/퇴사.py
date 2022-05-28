DP = []


def Backtracking(arr, index, value):
    if index >= N:
        DP.append(value)
        return

    next = index + arr[index][0]
    Backtracking(arr, next,
                 value + arr[index][1])  # 집는 경우
    next = index + 1
    Backtracking(arr, next, value)  # 집지 않는 경우


N = int(input())
arr = [] * N

for i in range(N):
    t, p = map(int, input().split())
    if i + t > N:  # 상담 불가능하면 가치를 0으로 만들기
        p = 0
    arr.append((t, p))

max_profit = Backtracking(arr, 0, 0)

print(max(DP))
