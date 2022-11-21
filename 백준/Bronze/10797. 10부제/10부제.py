N = input()
arr = list(map(str, input().split()))
print(len([x for x in arr if x == N]))