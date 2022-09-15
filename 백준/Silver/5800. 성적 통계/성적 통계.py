K = int(input())

for i in range(1, K+1):
    print(f"Class {i}")
    scores = list(map(int, input().split()))
    scores = sorted(scores[1:], reverse=True)
    max_score = scores[0]
    min_score = scores[-1]
    largest_gap = -1
    for i in range(1, len(scores)):
        gap = scores[i-1] - scores[i]
        if gap > largest_gap:
            largest_gap = gap
    print(f"Max {max_score}, Min {min_score}, Largest gap {largest_gap}")
