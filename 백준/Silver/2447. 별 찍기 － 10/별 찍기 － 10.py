def Star(N):
    if N <= 3:
        return ['***', '* *', '***']

    else:
        pattern = Star(N//3)
        new_pattern = []
        for level in ['top', 'mid', 'bottom']:
            for ch in pattern:
                if level == 'mid': # 중간에 구멍뚫기
                    ch = ch + " " * (N//3) + ch
                    new_pattern.append(ch)
                else:
                    ch = ch*3
                    new_pattern.append(ch)
        return new_pattern

N = int(input())
pattern = Star(N)
for p in pattern:
    print(p)