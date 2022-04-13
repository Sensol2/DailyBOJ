import sys
M = int(input())

S = []
for i in range(M):
    command = sys.stdin.readline().rstrip()
    if "add" in command:
        c, x = command.split()
        x = int(x)
        if x not in S:
            S.append(x)
    if "remove" in command:
        c, x = command.split()
        x = int(x)
        if x in S:
            S.remove(x)
    if "check" in command:
        c, x = command.split()
        x = int(x)
        if x in S:
            print(1)
        else:
            print(0)
    if "toggle" in command:
        c, x = command.split()
        x = int(x)
        if x in S:
            S.remove(x)
        else:
            S.append(x)
    if "all" in command:
        S = list(range(1,21))
    if "empty" in command:
        S = []