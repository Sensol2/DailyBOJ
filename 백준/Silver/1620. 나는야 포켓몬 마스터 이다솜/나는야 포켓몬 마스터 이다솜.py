import sys
N, M = map(int, input().split())
name_dict = dict()
num_dict = dict()
for i in range(1, N+1):
    ch = input()
    name_dict[i] = ch
    num_dict[ch] = i

for i in range(M):
    ch = sys.stdin.readline().strip()
    if ch.isdigit():
        print(name_dict[int(ch)])
    else:
        print(num_dict[ch])