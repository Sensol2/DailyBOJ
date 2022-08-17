N = int(input())
postfix = list(input())
term = dict()
for i in range(65, 65+N):  # 아스키 'A': 65
    term[chr(i)] = int(input())

for idx, p in enumerate(postfix):  # 알파벳을 숫자로 치환
    if p not in ['+', '-', '*', '/']:
        postfix[idx] = term[p]

stack = []
for ch in postfix:
    if ch in ['+', '-', '*', '/']:
        b = stack.pop()
        a = stack.pop()
        if ch == '+':
            stack.append(a+b)
        elif ch == '-':
            stack.append(a-b)
        elif ch == '*':
            stack.append(a*b)
        elif ch == '/':
            stack.append(a/b)
    else:
        stack.append(ch)

print("%.2f" % (stack.pop()))
