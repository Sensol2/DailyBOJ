def solution(N):
    if N == 1:
        return 2

    return solution(N-1) + divided_lines[N]+1

def get_divided_lines():
    count = 2
    divided_lines[1] = 1
    divided_lines[2] = 1
    for i in range(3, N+1):
        divided_lines[i] = count

        if i % 3 == 0:
            continue
        
        count += 1

N = int(input())
divided_lines = dict()
get_divided_lines()
print(solution(N))