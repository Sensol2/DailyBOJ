import sys, time

s = sys.stdin.readline()
idx = ord('a')
while True:
	print(s.find(chr(idx)), end=' ')
	idx += 1
	if chr(idx) == 'z':
		print(s.find(chr(idx)), end='')
		break
