A, B, C = map(int, input().split())

if A == B and A == C:
    print(10000+A*1000)
elif A == B:
    print(1000+A*100)
elif A == C:
    print(1000+A*100)
elif B == C:
    print(1000+B*100)
else:
    arr = [A, B, C]
    print(max(arr)*100)