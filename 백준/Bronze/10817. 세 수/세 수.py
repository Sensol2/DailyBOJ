A, B, C = map(int, input().split())
lst = [A, B, C]
lst.pop(lst.index(max(lst)))
print(max(lst))