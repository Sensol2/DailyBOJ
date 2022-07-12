n = int(input())
lines = []
for i in range(n):
    a, b = map(int, input().split())
    lines.append([a, b])

# 전깃줄 시작점 번호(1~n) 에 따라 순서대로 정렬하기
lines = sorted(lines, key=lambda x: x[0])
arr = [x[1] for x in lines]

# 전깃줄의 도착점 숫자 기준으로 LIS 알고리즘 (최장부분증가수열) 구하기
DP = [1] * n
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            DP[i] = max(DP[i], DP[j] + 1)

print(n - max(DP))
