N = int(input())

words = []
for i in range(N):
    word = input()
    words.append((len(word), word))
words = sorted(words, key=lambda x : (x[0], x[1]))
words = list(dict.fromkeys(words))
for word in words:
    print(word[1])