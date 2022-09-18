n = int(input())

persons = dict()
for i in range(n):
    name, day, month, year = input().split()
    persons[name] = [int(year), int(month), int(day)]

result = sorted(persons.items(), key=lambda x: (x[1][0], x[1][1], x[1][2]))
print(result[-1][0])
print(result[0][0])
