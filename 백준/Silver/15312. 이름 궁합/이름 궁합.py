A = list(input())
B = list(input())

stroke = {"A": 3, "B": 2, "C": 1, "D": 2, "E": 3, "F": 3, "G": 2, "H": 3, "I": 3, "J": 2, "K": 2, "L": 1,
          "M": 2, "N": 2, "O": 1, "P": 2, "Q": 2, "R": 2, "S": 1, "T": 2, "U": 1, "V": 1, "W": 1, "X": 2, "Y": 2, "Z": 1}

lst = []
for i in range(len(A)):
    lst.append(stroke[A[i]])
    lst.append(stroke[B[i]])

while len(lst) > 2:
    new_lst = []
    for i in range(1, len(lst)):
        new_lst.append((lst[i-1] + lst[i]) % 10)
    lst = new_lst

print(''.join(map(str, lst)))