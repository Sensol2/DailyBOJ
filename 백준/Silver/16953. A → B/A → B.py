def Backtracking(num, target, depth):
    if num == target:
        print(depth)
        global found
        found = True
        return
    if num > target:
        return

    # 2를 곱한다
    Backtracking(num*2, target, depth+1)
    # 1을 맨 뒤에 붙인다
    Backtracking(int(str(num)+'1'), target, depth+1)


found = False
A, B = map(int, input().split())
Backtracking(A, B, 1)
if not found:
    print("-1")
