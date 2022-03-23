n = int(input())

for i in range(n):
    n, m = map(int, input().split())
    docs = list(input().split())
    count = 0
    while True:
        if docs[0] >= max(docs):
            docs.pop(0)
            count += 1
            if m == 0:
                print(count)
                break

            m -= 1
        else:
            t = docs.pop(0)
            docs.append(t)
            if m == 0:
                m = len(docs) - 1
            else:
                m -= 1
    