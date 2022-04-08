import itertools
from collections import deque
from collections import Counter
import re

N = int(input())
words = []
for i in range(N):
    word = input()
    words.append(word)

concat_word = ""
for word in words:
    concat_word += word

elements = list(Counter("".join(concat_word)))
sequence = list(range(10-len(elements), 10))

priority_score = dict.fromkeys(elements, 0)

for word in words:
    for e in elements:
        score = 0
        exponent = len(word)-1
        for idx, ch in enumerate(word):
            if ch == e:
                score += 10**(exponent-idx)
        priority_score[e] += score

priority_score = sorted(priority_score.values(), reverse=True)
sequence = sorted(sequence, reverse=True)

result = 0
for idx, score in enumerate(priority_score):
    result += score * sequence[idx]
print(result)