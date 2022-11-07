import sys
input = sys.stdin.readline

N = int(input())
numbers = input()

all_sumv = 0

tmp_buffer = ""
for n in numbers:
    if n.isdigit():
        tmp_buffer += n
    else:
        all_sumv += int(tmp_buffer)
        tmp_buffer = ""

small_sumv = (N-1) * N // 2
print(abs(all_sumv - small_sumv))