X = list(map(int, list(input())))

count = 0
if sum(X) >= 10:
    count += 1
while sum(X) >= 10:
    X = sum(X)
    X = list(map(int, list(str(X))))
    count += 1

print(count)
if sum(X) % 3 == 0:
    print("YES")
else:
    print("NO")
