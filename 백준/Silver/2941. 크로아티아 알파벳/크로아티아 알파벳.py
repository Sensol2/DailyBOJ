import sys, time

s = sys.stdin.readline().strip()
for i in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
    s = s.replace(i, 'a')
print(len(s))