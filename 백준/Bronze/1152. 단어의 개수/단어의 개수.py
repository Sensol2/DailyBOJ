import sys, time

s = sys.stdin.readline()
splited = list(s.split(' '))
if '' in splited:
	splited.remove('')
if ' ' in splited:
	splited.remove(' ')
if '\n' in splited:
	splited.remove('\n')
print(len(splited))