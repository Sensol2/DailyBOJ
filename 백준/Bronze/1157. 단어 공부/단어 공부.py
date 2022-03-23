import sys, time

t = sys.stdin.readline()
t_dict = dict()
for i in range(ord('A'), ord('Z')+1):
	cnt = t.count(chr(i))
	t_dict[chr(i)] = cnt

for i in range(ord('a'), ord('z')+1):
	cnt = t.count(chr(i))
	t_dict[chr(i-32)] += cnt

best = max(t_dict.values())
if list(t_dict.values()).count(best) >= 2:
	print("?")
else:
	for key, value in t_dict.items():
		if (value == best):
			print(key)