import math
A, B, N = map(int, input().split())
A = (A - B*(A // B)) * 10
for i in range(N-1):
    A = (A - B*(A // B)) * 10
print(A // B)