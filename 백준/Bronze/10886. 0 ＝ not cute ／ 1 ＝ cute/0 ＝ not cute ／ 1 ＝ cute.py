n = int(input())
lst = [int(input()) for i in range(n)]
if lst.count(0) > lst.count(1):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
