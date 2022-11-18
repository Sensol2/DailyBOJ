import math
import sys

input = sys.stdin.readline


def CreateTable(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        if table[i] != 0:  # 이미 table에 값 있으면 넘기기
            continue

        if pattern[i] != pattern[j]:  # 불일치하면 j 내리기
            table[i] = 0
            if j > 0:
                j -= 1
            continue

        if pattern[i] == pattern[j]:  # 일치하면
            for k in range(i, len(pattern)):  # 일치하는 곳까지 j 증가시키며 table 값 추가
                if pattern[k] == pattern[j]:
                    j += 1
                    table[k] = j
                else:
                    j = table[j-1]
                    break
    return table


def KMP(parent, pattern):
    match_count = 0
    index_arr = []

    table = CreateTable(pattern)

    parent_size = len(parent)
    pattern_size = len(pattern)
    j = 0
    for i in range(0, parent_size):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j-1]

        if parent[i] == pattern[j]:
            if j == pattern_size - 1:  # 문자열을 찾았을 때
                index_arr.append(i - pattern_size + 2)
                match_count += 1
                j = table[j]
            else:
                j += 1
    return match_count, index_arr


N = int(input())
meat_roulette = input().split()
curr_roulette = input().split()


count, idxs = KMP(curr_roulette + curr_roulette[:-1], meat_roulette)


gcd_result = math.gcd(count, N)

count = count // gcd_result
N = N // gcd_result

print(f"{count}/{N}")
