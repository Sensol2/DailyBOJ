burger = []
beverage = []
for i in range(5):
    if i <= 2:
        burger.append(int(input()))
    else:
        beverage.append(int(input()))
print(min(burger) + min(beverage) - 50)
