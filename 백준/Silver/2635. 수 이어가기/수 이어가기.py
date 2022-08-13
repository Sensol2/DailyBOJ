def BackTracking(num):
    a = N
    b = num
    sequence = [a, b]
    while True:
        tmp = b
        b = a-b
        a = tmp
        if b < 0:
            break
        sequence.append(b)
    return sequence


N = int(input())
max_num = -1
max_sequence = []
for i in range(1, N+1):
    s = BackTracking(i)
    if len(s) > max_num:
        max_num = len(s)
        max_sequence = s
print(max_num)
print(' '.join(map(str, max_sequence)))
