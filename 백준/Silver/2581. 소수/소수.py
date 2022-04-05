scale = 10000
numbers = list(range(0,scale+1,1))
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

for num in prime_numbers:
    tmp = num + num
    while tmp <= scale:
        numbers[tmp] = 0
        tmp += num
numbers[1] = 0 # 1은 소수가 아니다

M = int(input())
N = int(input())

arr = []
noPrimeNum = True
for i in range(M, N+1):
    if numbers[i] != 0:
        noPrimeNum = False
        arr.append(numbers[i])
if noPrimeNum:
    print(-1)
else:
    print(sum(numbers[M:N+1]))
    print(min(arr))
