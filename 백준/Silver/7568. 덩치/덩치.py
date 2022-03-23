num = int(input())
xylist = [] 
for i in range(num):
    x, y = map(int, input().split())
    xylist.append([x, y])

ranking = [0] * num
for i in range(num):
    w = xylist[i][0] 
    h = xylist[i][1]
    for j in range(num):
        tw = xylist[j][0]
        th = xylist[j][1]

        if tw > w and th > h:
            ranking[i] += 1
    ranking[i] += 1

for i in ranking:
    print(i, end=' ')
