import sys, math
U, N = map(int,input().split())

auction = [[] for _ in range(U+1)]

for i in range(N):
    S, P = sys.stdin.readline().rstrip().split()
    P = int(P)
    auction[P].append((S, P))

winner = None
min_Participant = math.inf
for i in range(U):
    if not auction[i]: 
        continue
    if len(auction[i]) < min_Participant:
        min_Participant = len(auction[i])
        winner = auction[i][0]
print(winner[0], winner[1])