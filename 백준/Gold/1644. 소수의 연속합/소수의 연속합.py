def TwoPointer(arr, N):  # 리스트 arr에서 부분합이 N이 되는 경우의 수를 리턴
    count = 0
    end = 0
    sum_value = 0

    for start in range(len(arr)):
        # end를 가능한 곳까지 이동시키기
        while sum_value < N and end < len(arr):
            sum_value += arr[end]
            end += 1
        if sum_value == N:
            count += 1
        sum_value -= arr[start]

    return count


N = int(input())
SIZE = 4000000
DP = [0] * SIZE
prime_number = []
for i in range(2, SIZE):
    if DP[i] == 0:
        prime_number.append(i)
        for j in range(i*2, SIZE, i):
            DP[j] = 1
print(TwoPointer(prime_number, N))
