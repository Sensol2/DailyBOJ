N = int(input())
num_dict = dict()
arr = list(map(int, input().split()))
for num in arr:
    num_dict[num] = True

arr = sorted(num_dict.keys())
print(' '.join(map(str, arr)))