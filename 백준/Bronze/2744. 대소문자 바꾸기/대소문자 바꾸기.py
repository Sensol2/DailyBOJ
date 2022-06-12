arr = list(input())

for ch in arr:
    if ch.isupper():
        print(ch.lower(), end='')
    if ch.islower():
        print(ch.upper(), end='')
