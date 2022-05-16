arr = list(input())

stack = []
IPC = {'(': 0, '+': 3, '-': 3, '*': 2, '/': 2, '%': 2}
ISP = {'(': 8, '+': 3, '-': 3, '*': 2, '/': 2, '%': 2}
for i in arr:
    if i.isalpha():  # 알파벳이면 그냥 출력
        print(i, end='')
    else:  # 아니면 스택에 넣기
        stack.append(i)
        if i == ')':  # 닫는 괄호 나오면 괄호 사이 연산자 모두 출력
            while True:
                j = stack.pop()
                if j != '(' and j != ')':
                    print(j, end='')
                if j == '(':
                    break
        while len(stack) >= 2 and ISP[stack[-2]] <= IPC[stack[-1]]:
            j = stack.pop(len(stack)-2)
            print(j, end='')

while stack:  # 남은 스택 다 비우기
    print(stack.pop(), end='')
