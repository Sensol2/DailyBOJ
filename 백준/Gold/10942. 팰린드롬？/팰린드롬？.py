import sys
input = sys.stdin.readline


def isPalindrome(s, e):
    while s < e:
        if arr[s] != arr[e]:
            return 0
        else:
            s += 1
            e -= 1
    return 1


N = int(input())
arr = list(map(int, input().split()))
size = len(arr)
DP = [[0] * size for _ in range(size)]

for i in range(size):
    # 홀수인 경우
    left = i
    right = i
    while True:
        if -1 < left and right < size:
            if arr[left] == arr[right]:
                DP[left][right] = 1
                left -= 1
                right += 1
            else:
                break
        else:
            break
    # 짝수인 경우
    left = i
    right = i+1
    while True:
        if -1 < left and right < size:
            if arr[left] == arr[right]:
                DP[left][right] = 1
                left -= 1
                right += 1
            else:
                break
        else:
            break

M = int(input())
for i in range(M):
    S, E = map(int, input().split())
    S, E = S-1, E-1  # 0부터 시작하는 인덱스로 바꾸기 위해서
    print(DP[S][E])
