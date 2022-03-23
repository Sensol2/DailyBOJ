import sys, time

n = int(sys.stdin.readline())

cnt = 0
for i in range(n):
    s = sys.stdin.readline()
    curr_ch = s[0]
    ch_dict = []
    isGroupWord = True
    for ch in s:
        if curr_ch == ch:
            ch_dict.append(ch)
        else:
            if ch in ch_dict:
                isGroupWord = False
                break
            ch_dict.append(ch)
            curr_ch = ch
    if isGroupWord:
        cnt+=1
print(cnt)
