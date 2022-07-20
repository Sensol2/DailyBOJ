from collections import deque


def roundTraditional(val, digits):  # 사사오입
    return round(val+10**(-len(str(val))-1), digits)


n = int(input())
scores = []

for i in range(n):
    scores.append(int(input()))
scores = deque(sorted(scores))

exceptPeson = roundTraditional(len(scores)*0.15, 0)
for i in range(int(exceptPeson)):
    scores.popleft()
    scores.pop()

if n == 0:
    print("0")
else:
    result = int(roundTraditional(sum(scores)/len(scores), 0))
    print(result)
