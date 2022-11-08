word = input()
results = []
for i in range(len(word)):
    for j in range(i+1, len(word)):
        for j in range(j+1, len(word)):
            ch1 = word[0:i+1]
            ch2 = word[i+1:j]
            ch3 = word[j:len(word)+1]

            rch1 = "".join(reversed(ch1))
            rch2 = "".join(reversed(ch2))
            rch3 = "".join(reversed(ch3))

            results.append(rch1+rch2+rch3)
print(sorted(results)[0])
