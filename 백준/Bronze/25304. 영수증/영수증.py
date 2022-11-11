
sum_v = int(input())
acc_v = 0
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    acc_v += a*b

if sum_v == acc_v:
    print("Yes")
else:
    print("No")
