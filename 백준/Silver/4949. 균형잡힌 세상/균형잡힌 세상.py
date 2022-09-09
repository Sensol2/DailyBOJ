def Check(brackets):
    stack = []
    while brackets:
        bracket = brackets.pop()
        if bracket in [')', ']']:
            stack.append(bracket)
        else:
            if stack:
                item = stack.pop()
                if bracket == '(' and item != ')':
                    return False
                if bracket == '[' and item != ']':
                    return False
            else:
                return False
    if stack:
        return False
    return True


while True:
    strings = input()
    if strings == '.':
        break

    brackets = []
    for ch in strings:
        if ch in ['(', ')', '[', ']']:
            brackets.append(ch)

    res = Check(brackets)
    if res:
        print("yes")
    else:
        print("no")
