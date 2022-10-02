from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


def fill_padding(ch, num):
    pattern = ch
    if len(ch) < num:
        i = 0
        while len(ch) < num:
            ch += pattern
            i += len(pattern)
    return ch


s = input()
t = input()

num = lcm(len(s), len(t))

s = fill_padding(s, num)
t = fill_padding(t, num)

if s == t:
    print(1)
else:
    print(0)
