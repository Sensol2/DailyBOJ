h, m = map(int, input().split())

minute = h * 60 + m
result = minute - 45

if result >=0:
	print(result//60, result%60)
else:
	newresult = 1440+result
	print(newresult//60, newresult%60)