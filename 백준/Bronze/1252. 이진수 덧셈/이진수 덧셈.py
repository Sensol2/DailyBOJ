A, B = input().split()
A = '0b' + A
B = '0b' + B
print(bin(int(A,2)+int(B,2)).replace('0b', ''))