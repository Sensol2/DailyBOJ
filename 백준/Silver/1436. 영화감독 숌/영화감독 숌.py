my_dict = dict()

N = int(input())
count = 0
for i in range(2666800):
    if '666' in str(i):
        my_dict[count] = i
        count += 1
print(my_dict[N-1])
