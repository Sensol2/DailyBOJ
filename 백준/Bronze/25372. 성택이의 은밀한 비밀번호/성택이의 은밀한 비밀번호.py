# 6자리 이상 9자리 이하
N = int(input())
for i in range(N):
    ch = input()
    if len(ch) >= 6 and len(ch) <= 9:
        print("yes")
    else:
        print("no")