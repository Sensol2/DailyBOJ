while True:
    sentence = list(input())
    if sentence[0] == '#':
        break
    count = 0
    for c in sentence:
        if c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            count += 1
    print(count)
