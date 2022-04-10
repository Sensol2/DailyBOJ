import math
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    arr = [a, b, c]
    hypothesis = max(arr)
    arr.remove(hypothesis)

    if hypothesis == math.sqrt(arr[0]**2 + arr[1]**2):
        print("right")
    else:
        print("wrong")