import sys
input = sys.stdin.readline

def sol():
    result = []
    stack = [0]
    count = 0
    for i in range(n):
        if i == 0:
            while arr[i] != stack[-1]:
                count += 1
                stack.append(count)
                result.append("+")

        if arr[i] < stack[-1]: # pop
            while arr[i] != stack[-1]:
                stack.pop()
                result.append("-")
        
        elif stack[-1] < arr[i] : # append
            if arr[i] < count:
                return ["NO"]
            while arr[i] != stack[-1]:
                count += 1
                stack.append(count)
                result.append("+")

        if arr[i] == stack[-1]:
            stack.pop()
            result.append("-")

    return result

n = int(input())
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)


result = sol()
for r in result:
    print(r)